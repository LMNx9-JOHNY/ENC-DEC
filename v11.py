""" Codded By DARK LMNx9 """

import os,sys,time,subprocess

ENC_DEC = os.path.dirname(os.path.abspath(globals().get("__file__", ".")))
if ENC_DEC not in sys.path:sys.path.insert(0, ENC_DEC)

DARK = os.uname().machine.lower()
LMNx9 = sys.version_info[:2] >= (3, 14)
TG = "https://t.me/+6hZVa9jGrIY4ZDRl"
SO = ENC_DEC + "/v11.so"

def lmnXclr():sys.stdout.write("\033[H\033[2J\033[3J");sys.stdout.flush()
def lmnXopn():
    for c in (["termux-open-url",TG],["am","start","-a","android.intent.action.VIEW","-d",TG],["xdg-open",TG]):
        try:
            if subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=3).returncode==0:return
        except Exception:pass
def lmnXout(m,cd=1):
    lmnXclr();print("\a\n"+m,flush=True);lmnXopn();time.sleep(1);sys.exit(cd)

def lmnXrun():
    if DARK in ('aarch64', 'arm64') and LMNx9:
        if not os.path.isfile(SO):
            lmnXout("</> LMNx9 ENC-DEC v11 Souce Not Found: v11.so Missing..!"
                "\n</> Make Sure (v11.so) Existing In Same Directory"
                "\n</> Looked In: " + SO)
        try:import v11
        except (ImportError, OSError) as x:
            lmnXout("</> LMNx9 ENC-DEC v11 Souce Not Found: " + str(x) +
                "\n</> Make Sure (v11.so) Existing In Same Directory"
                "\n</> Looked In: " + SO)
        Sukhi = getattr(v11, "main", None) or getattr(v11, "run", None)
        if Sukhi:Sukhi()
        else:lmnXout("</> v11 Loaded But No main()/run() Entry Point Found..!",2)

    elif DARK in ('aarch64', 'arm64') and not LMNx9:
        lmnXout("</> Only Python 3.14 Android Linux Terminal Supported..!"
            "\n</> Your Python Version: " + sys.version.split()[0])

    elif DARK in ('armv7l', 'armv8l', 'i686', 'i386', 'x86'):
        lmnXout("</> Only Android arm64 (64bit) Supported..!"
            "\n</> Device Arch: " + DARK +
            "\n</> Your Device Not Supported For Run This Tool..!")

    else:
        lmnXout("</> Only Python 3.14 Android 64bit Linux Terminal Supported..!"
            "\n</> Device Arch: " + DARK +
            "\n</> Your Device Not Supported For Run This Tool..!")

if __name__ == "__main__":
    try:lmnXrun()
    except SystemExit:raise
    except BaseException as e:
        import traceback
        lmnXclr();print("\a\n</> LMNx9 ERROR: " + type(e).__name__ + ": " + str(e),flush=True)
        traceback.print_exc();sys.stdout.flush();sys.exit(3)
        