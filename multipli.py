import asyncio
import random
from loguru import logger
from web3 import AsyncWeb3
import settings
from client import Client
import models


class MultiPli:
    def __init__(self, client: Client):
        self.client = client

        self.contract_claim = self.client.w3.eth.contract(
            address=AsyncWeb3.to_checksum_address('0x181579497d5c4EfEC2424A21095907ED7d91ac9A'),
            abi=models.AbIs.multipl
        )

        self.contract_usdc = self.client.w3.eth.contract(
            address=AsyncWeb3.to_checksum_address('0x924f1bf31b19a7f9695f3fc6c69c2ba668ea4a0a'),
            abi=models.AbIs.usdc
        )

        self.contract_spender = self.client.w3.eth.contract(
            address=AsyncWeb3.to_checksum_address('0xbcf1415bd456edb3a94c9d416f9298ecf9a2cdd0'),
            abi=models.AbIs.multipl
        )

    async def claim_usdc(self):
        try:
            wait_time = random.randint(settings.TIME_AWAIT[0], settings.TIME_AWAIT[1])
            logger.info(
                f'Profile: {self.client.profile} Начну работу через {wait_time} секунд')
            await asyncio.sleep(wait_time)

            logger.info(f'Profile: {self.client.profile} {self.client.account.address} Проверяю баланс USDC')
            token_balance = await self.contract_usdc.functions.balanceOf(self.client.account.address).call()
            logger.info(
                f'Profile: {self.client.profile} {self.client.account.address} Баланс USDC: {token_balance / 10 ** 6}')

            if token_balance > 0:
                logger.info(
                    f'Profile: {self.client.profile} {self.client.account.address} Клейм не требуется')
                return token_balance
            logger.info(
                f'Profile: {self.client.profile} {self.client.account.address} Отправляю транзакцию')
            tx = await self.client.send_transaction(
                to=self.contract_claim.address,
                data=self.contract_claim.encode_abi('claimToken', args=([self.contract_usdc.address]))
            )

            if tx:
                try:
                    await self.client.verif_tx(tx_hash=tx)
                    logger.success(
                        f'Profile: {self.client.profile} {self.client.account.address} Transaction success!! tx_hash: 0x{tx.hex()}')
                except Exception as err:
                    logger.warning(
                        f'Profile: {self.client.profile} {self.client.account.address} Transaction error!! tx_hash: 0x{tx.hex()}; error: {err}')
                    raise ValueError(f'{self.client.profile} Ошибка транзакции')
            else:
                logger.error(f'Profile: {self.client.profile} {self.client.account.address} Transaction error!!!')
                raise ValueError(f'{self.client.profile} Ошибка транзакции')
        except Exception as er:
            logger.error(f'Profile: {self.client.profile} {self.client.account.address} {er}')

    async def approve_usdc(self):
        try:
            wait_time = random.randint(settings.TIME_AWAIT[0], settings.TIME_AWAIT[1])
            logger.info(
                f'Profile: {self.client.profile} Начну работу через {wait_time} секунд')
            await asyncio.sleep(wait_time)

            logger.info(
                f'Profile: {self.client.profile} {self.client.account.address} Делаю approve...')
            token_balance = await self.contract_usdc.functions.balanceOf(self.client.account.address).call()
            approved_amount = await self.contract_usdc.functions.allowance(self.client.account.address,
                                                                           self.contract_spender.address).call()

            if approved_amount < token_balance:
                tx = await self.client.send_transaction(
                    to=self.contract_usdc.address,
                    data=self.contract_usdc.encode_abi('approve',
                                                       args=(
                                                           self.contract_spender.address,
                                                           token_balance
                                                       ))
                )

                if tx:
                    try:
                        await self.client.verif_tx(tx_hash=tx)
                        logger.success(
                            f'Profile: {self.client.profile} {self.client.account.address} Transaction success!! tx_hash: 0x{tx.hex()}')
                    except Exception as err:
                        logger.warning(
                            f'Profile: {self.client.profile} {self.client.account.address} Transaction error!! tx_hash: 0x{tx.hex()}; error: {err}')
                        raise ValueError(f'{self.client.profile} Ошибка транзакции')
                else:
                    logger.error(
                        f'Profile: {self.client.profile} {self.client.account.address} Transaction error!!!')
                    raise ValueError(f'{self.client.profile} Ошибка транзакции')
            else:
                logger.info(
                    f'Profile: {self.client.profile} {self.client.account.address} Approve не нужен')
        except Exception as er:
            logger.error(f'Profile: {self.client.profile} {self.client.account.address} {er}')

    async def stake_usdc(self):
        try:
            wait_time = random.randint(settings.TIME_AWAIT[0], settings.TIME_AWAIT[1])
            logger.info(
                f'Profile: {self.client.profile} Начну работу через {wait_time} секунд')
            await asyncio.sleep(wait_time)

            logger.info(
                f'Profile: {self.client.profile} {self.client.account.address} Стейкаю USDC')
            token_balance = await self.contract_usdc.functions.balanceOf(self.client.account.address).call()
            tx = await self.client.send_transaction(
                to=self.contract_spender.address,
                data=self.contract_spender.encode_abi('deposit',
                                                      args=(
                                                          [self.contract_usdc.address,
                                                           random.randint(500000, token_balance)]
                                                      ))
            )

            if tx:
                try:
                    await self.client.verif_tx(tx_hash=tx)
                    logger.success(
                        f'Profile: {self.client.profile} {self.client.account.address} Transaction success!! tx_hash: 0x{tx.hex()}')
                except Exception as err:
                    logger.warning(
                        f'Profile: {self.client.profile} {self.client.account.address} Transaction error!! tx_hash: 0x{tx.hex()}; error: {err}')
                    raise ValueError(f'{self.client.profile} Ошибка транзакции')
            else:
                logger.error(
                    f'Profile: {self.client.profile} {self.client.account.address} Transaction error!!!')
                raise ValueError(f'{self.client.profile} Ошибка транзакции')
        except Exception as er:
            logger.error(f'Profile: {self.client.profile} {self.client.account.address} {er}')
