import sys, os
## Code to disable creating pycache dir after running
sys.dont_write_bytecode = True

sys.path.append(os.path.abspath(f"{os.getcwd()}/src/redhat_assisted_installer/"))

import redhat_assisted_installer.assistedinstaller as assistedinstaller

installer = assistedinstaller.assistedinstaller()

installer.postInfrastructureEnvironment("testing-infra", version="4.15")