from plasma_cash.root_chain.deployer import Deployer
from integration_tests.erc20.deployer import Erc20Deployer

Deployer().deploy_contract('RootChain/RootChain.sol')
Erc20Deployer().deploy_contract('PlasmaCashToken/PlasmaCashToken.sol')
