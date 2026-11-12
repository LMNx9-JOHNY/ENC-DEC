<p align="center">
<img src="https://img.shields.io/badge/All_In_One_Hardcode_Encoder_%26_Decoder-7c3aed?style=for-the-badge&labelColor=0f172a&logo=python&logoColor=white" alt="All In One Hardcode Encoder & Decoder"/>
</p>

<p align="center">
<img src="https://raw.githubusercontent.com/LMNx9-JOHNY/LMNx9_ENC/refs/heads/main/v11.png" width="720" alt="LMNx9 ENC DEC v11"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/LMNx9%20ENC--DEC%20v11-0e7490?style=for-the-badge&labelColor=0f172a&logo=gnubash&logoColor=white" alt="LMNx9 ENC-DEC v11"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Version-v11.0-0f172a?style=for-the-badge&labelColor=0f172a&color=0e7490&logo=git&logoColor=white" alt="Version"/>
<img src="https://img.shields.io/badge/Encoders-29-0f172a?style=for-the-badge&labelColor=0f172a&color=7c3aed&logo=python&logoColor=white" alt="Encoders"/>
<img src="https://img.shields.io/badge/Decoders-29-0f172a?style=for-the-badge&labelColor=0f172a&color=be185d&logo=python&logoColor=white" alt="Decoders"/>
<img src="https://img.shields.io/badge/Arch-arm64--v8a-0f172a?style=for-the-badge&labelColor=0f172a&color=15803d&logo=arm&logoColor=white" alt="Arch"/>
<img src="https://img.shields.io/badge/Python-3.14-0f172a?style=for-the-badge&labelColor=0f172a&color=b45309&logo=python&logoColor=white" alt="Python"/>
</p>

<p align="center">
<a href="https://t.me/+6hZVa9jGrIY4ZDRl"><img src="https://img.shields.io/badge/Join_Telegram-1d4ed8?style=for-the-badge&logo=telegram&logoColor=white" alt="Join Telegram"/></a>
<a href="https://t.me/x_LMNx9"><img src="https://img.shields.io/badge/Developer-7c3aed?style=for-the-badge&logo=telegram&logoColor=white" alt="Developer"/></a>
<a href="https://lmnx9.shop"><img src="https://img.shields.io/badge/Website-be185d?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"/></a>
</p>

---

<p align="center">
<img src="https://img.shields.io/badge/Why_LMNx9-0f172a?style=for-the-badge&labelColor=0f172a&color=0e7490&logo=android&logoColor=white" alt="Why LMNx9 ENC-DEC"/>
</p>

| <img src="https://img.shields.io/badge/Icon-0e7490?style=flat-square" alt="Icon"/> | <img src="https://img.shields.io/badge/Feature-7c3aed?style=flat-square" alt="Feature"/> | <img src="https://img.shields.io/badge/Details-be185d?style=flat-square" alt="Details"/> |
|:--:|:--|:--|
| <img src="https://img.shields.io/badge/_-7c3aed?style=flat-square&logo=python&logoColor=white" alt=""/> | **58 Reversible Paths** | 29 encoders, each with an exact decoder |
| <img src="https://img.shields.io/badge/_-0e7490?style=flat-square&logo=arm&logoColor=white" alt=""/> | **Native Engine** | `v11.so` arm64 core, Python only as launcher |
| <img src="https://img.shields.io/badge/_-15803d?style=flat-square&logo=linux&logoColor=white" alt=""/> | **Chain Depth 1–150** | Stack layers at runtime, default `5` |
| <img src="https://img.shields.io/badge/_-b45309?style=flat-square&logo=github&logoColor=white" alt=""/> | **Integrity Tags** | HMAC-SHA256 on AES and XOR, verified on decode |
| <img src="https://img.shields.io/badge/_-1d4ed8?style=flat-square&logo=pypi&logoColor=white" alt=""/> | **Auto Dependencies** | Missing packages install with a live progress bar |
| <img src="https://img.shields.io/badge/_-be185d?style=flat-square&logo=cmake&logoColor=white" alt=""/> | **Real Compilers** | Cython `.so` builds and PyInstaller binaries |
| <img src="https://img.shields.io/badge/_-4338ca?style=flat-square&logo=android&logoColor=white" alt=""/> | **Termux Native** | Storage setup runs itself, output lands in `/sdcard` |

---

<p align="center">
<img src="https://img.shields.io/badge/Quick_Start-0f172a?style=for-the-badge&labelColor=0f172a&color=7c3aed&logo=gnubash&logoColor=white" alt="Installation"/>
</p>


**1. Update Termux**

```bash
    pkg update -y && pkg upgrade -y
```

**2. Install required tools**

```bash
    pkg install -y python clang make cmake termux-tools git
```

**3. Clone the repository**

```bash
    git clone --depth=1 https://github.com/LMNx9-JOHNY/ENC-DEC
    cd ENC-DEC && chmod +x *
```

**4. Run**

```bash
    python v11.py
```

---

<p align="center">
<img src="https://img.shields.io/badge/Usage-0f172a?style=for-the-badge&labelColor=0f172a&color=be185d&logo=linux&logoColor=white" alt="Usage"/>
</p>

| <img src="https://img.shields.io/badge/Step-be185d?style=flat-square" alt="Step"/> | <img src="https://img.shields.io/badge/Action-7c3aed?style=flat-square" alt="Action"/> |
|:--:|:--|
| **1** | Launch with `python v11.py` |
| **2** | Allow storage access when prompted |
| **3** | Pick a slot: `01–29` encode · `32–60` decode |
| **4** | Enter a file path or paste payload |
| **5** | Set chain depth `1–150` (empty = `5`) |

| <img src="https://img.shields.io/badge/Mode-0e7490?style=flat-square" alt="Mode"/> | <img src="https://img.shields.io/badge/Output_pattern-15803d?style=flat-square" alt="Output pattern"/> |
|:--|:--|
| Encode | `<name>_ENCv11.<ext>` |
| Decode | `dec_<name>.<ext>` |

---

<p align="center">
<img src="https://img.shields.io/badge/Supported_Formats-0f172a?style=for-the-badge&labelColor=0f172a&color=15803d&logo=html5&logoColor=white" alt="Supported Formats"/>
</p>

| <img src="https://img.shields.io/badge/Type-15803d?style=flat-square" alt="Type"/> | <img src="https://img.shields.io/badge/Extension-1d4ed8?style=flat-square" alt="Extension"/> | <img src="https://img.shields.io/badge/Slots-b45309?style=flat-square" alt="Slots"/> |
|:--|:--|:--|
| Python | `.py` / `.pyc` | 01–20, 22, 26–29 |
| Shell | `.sh` | 21 |
| HTML | `.html` / `.htm` | 23 |
| JavaScript | `.js` | 24 |
| PHP | `.php` | 25 |

---

<p align="center">
<img src="https://img.shields.io/badge/Encoder_Methods_·_Free-0f172a?style=for-the-badge&labelColor=0f172a&color=b45309&logo=python&logoColor=white" alt="Encoder Methods"/>
</p>

<details>
<summary><b>Show all 29 encoders</b></summary>

| <img src="https://img.shields.io/badge/%23-b45309?style=flat-square" alt="#"/> | <img src="https://img.shields.io/badge/Method-0e7490?style=flat-square" alt="Method"/> | <img src="https://img.shields.io/badge/%23-b45309?style=flat-square" alt="#"/> | <img src="https://img.shields.io/badge/Method-0e7490?style=flat-square" alt="Method"/> |
|:--:|:--|:--:|:--|
| 01 | Normal-Marshal | 16 | ELF-Obfuscate-X |
| 02 | Normal-Zlib | 17 | Cythonize-3.14 |
| 03 | Normal-Base16 | 18 | AES-256-Hashlib |
| 04 | Normal-Base32 | 19 | Pyinstaller-3.14 |
| 05 | Normal-Base64 | 20 | ROT13-armv32-64 |
| 06 | Zlib-Base16 | 21 | Bash-Obfuscator |
| 07 | Zlib-Base32 | 22 | ASCII-xN-armv64 |
| 08 | Zlib-Base64 | 23 | HTML-Obfuscator |
| 09 | Marshal-Zlib | 24 | JavaScript-OBF |
| 10 | Marshal-Base16 | 25 | PHP-Obfuscator |
| 11 | Marshal-Base32 | 26 | Hex-Bytecodes |
| 12 | Marshal-Base64 | 27 | LZMA-Compress |
| 13 | Marshal-Zlib-B16 | 28 | XOR-Cipher |
| 14 | Marshal-Zlib-B32 | 29 | Base85-Zlib |
| 15 | Marshal-Zlib-B64 | | |

</details>

---

<p align="center">
<img src="https://img.shields.io/badge/Decoder_Methods_·_VIP-0f172a?style=for-the-badge&labelColor=0f172a&color=1d4ed8&logo=python&logoColor=white" alt="Decoder Methods"/>
</p>

<details>
<summary><b>Show all 29 decoders</b></summary>

| <img src="https://img.shields.io/badge/%23-1d4ed8?style=flat-square" alt="#"/> | <img src="https://img.shields.io/badge/Method-7c3aed?style=flat-square" alt="Method"/> | <img src="https://img.shields.io/badge/%23-1d4ed8?style=flat-square" alt="#"/> | <img src="https://img.shields.io/badge/Method-7c3aed?style=flat-square" alt="Method"/> |
|:--:|:--|:--:|:--|
| 32 | Normal-Marshal | 47 | ELF-Obfuscate-X |
| 33 | Normal-Zlib | 48 | Cythonize-3.14 |
| 34 | Normal-Base16 | 49 | AES-256-Hashlib |
| 35 | Normal-Base32 | 50 | PyInstaller-3.14 |
| 36 | Normal-Base64 | 51 | ROT13-armv32-64 |
| 37 | Zlib-Base16 | 52 | Bash-Obfuscator |
| 38 | Zlib-Base32 | 53 | ASCII-xN-armv64 |
| 39 | Zlib-Base64 | 54 | HTML-Obfuscator |
| 40 | Marshal-Zlib | 55 | JavaScript-OBF |
| 41 | Marshal-Base16 | 56 | PHP-Obfuscator |
| 42 | Marshal-Base32 | 57 | Hex-Bytecodes |
| 43 | Marshal-Base64 | 58 | LZMA-Decompress |
| 44 | Marshal-Zlib-B16 | 59 | XOR-Cipher |
| 45 | Marshal-Zlib-B32 | 60 | Base85-Zlib |
| 46 | Marshal-Zlib-B64 | | |

> Slots `47`, `48` and `50` are unpack steps. The artifact is recovered, not regenerated byte-for-byte.

</details>

---

<p align="center">
<img src="https://img.shields.io/badge/VIP_Access-0f172a?style=for-the-badge&labelColor=0f172a&color=1d4ed8&logo=telegram&logoColor=white" alt="VIP Access"/>
</p>

| <img src="https://img.shields.io/badge/Step-1d4ed8?style=flat-square" alt="Step"/> | <img src="https://img.shields.io/badge/Action-7c3aed?style=flat-square" alt="Action"/> |
|:--:|:--|
| **1** | Run `python v11.py` and copy your Access Key |
| **2** | Send the key and your Termux username to the developer |
| **3** | Wait for approval |
| **4** | Enter the Verify Key on any decoder |
| **5** | License is cached locally and stays unlocked |

> Keys are bound to your username and device.

<p align="center">
<a href="https://t.me/x_LMNx9"><img src="https://img.shields.io/badge/Request_Access-1d4ed8?style=for-the-badge&logo=telegram&logoColor=white" alt="Request Access"/></a>
</p>

---

<p align="center">
<img src="https://img.shields.io/badge/Troubleshooting-0f172a?style=for-the-badge&labelColor=0f172a&color=b91c1c&logo=googlechrome&logoColor=white" alt="Troubleshooting"/>
</p>

<details>
<summary><b>Show common errors</b></summary>

| <img src="https://img.shields.io/badge/Message-b91c1c?style=flat-square" alt="Message"/> | <img src="https://img.shields.io/badge/Fix-15803d?style=flat-square" alt="Fix"/> |
|:--|:--|
| `FILE NOT FOUND` | Use the absolute path |
| `ONLY .PY FILES ALLOWED` | Match the slot's format |
| `FILE TOO SHORT` | File needs at least 2 lines |
| `Network Error` | Connect, then relaunch |
| `Cythonize Failed` | `pkg install clang cython make` |
| `PyInstaller Failed` | `pip install --force-reinstall pyinstaller` |
| `integrity check failed` | Payload was edited after encoding |
| `no .so for Python X.Y` | Install Python 3.14 |
| Link won't open | `pkg install termux-tools` |

</details>

---

<p align="center">
<img src="https://img.shields.io/badge/Disclaimer-0f172a?style=for-the-badge&labelColor=0f172a&color=a16207" alt="Disclaimer"/>
</p>

Verify every encoded output in a sandbox before deploying. The engine is closed-source and may change between builds.

---

<p align="center">
<img src="https://img.shields.io/badge/Contact-0f172a?style=for-the-badge&labelColor=0f172a&color=15803d&logo=whatsapp&logoColor=white" alt="Contact"/>
</p>

<table align="center">
<tr>
<td align="center" width="320">
<img src="https://api.iconify.design/lucide/send.svg?color=%2322d3ee&width=44" width="44" alt="Developer"/>
<h3>Developer</h3>
<a href="https://t.me/x_LMNx9"><img src="https://img.shields.io/badge/Telegram-@x__LMNx9-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Developer"/></a>
</td>
<td align="center" width="320">
<img src="https://api.iconify.design/lucide/users.svg?color=%2322d3ee&width=44" width="44" alt="Community"/>
<h3>Community</h3>
<a href="https://t.me/+6hZVa9jGrIY4ZDRl"><img src="https://img.shields.io/badge/Telegram-Join_Group-8b5cf6?style=for-the-badge&logo=telegram&logoColor=white" alt="Join Group"/></a>
</td>
</tr>
<tr>
<td align="center" width="320">
<img src="https://api.iconify.design/lucide/message-circle.svg?color=%2322d3ee&width=44" width="44" alt="WhatsApp"/>
<h3>WhatsApp</h3>
<a href="https://wa.me/19707808868"><img src="https://img.shields.io/badge/WhatsApp-+1_970_780_8868-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
</td>
<td align="center" width="320">
<img src="https://api.iconify.design/lucide/globe.svg?color=%2322d3ee&width=44" width="44" alt="Website"/>
<h3>Website</h3>
<a href="https://lmnx9.shop"><img src="https://img.shields.io/badge/Web-lmnx9.shop-ec4899?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"/></a>
</td>
</tr>
</table>

<p align="center"><sub>DARK LMNx9 TEAM · Built for Termux · Tested on arm64-v8a</sub></p>
