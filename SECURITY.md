# Security Policy,  SomloK / ESP32-DIV-KILAZ

## Scope

This document applies to the **SomloK firmware**, the **ESP32-DIV V2 flasher tool**, and any
scripts, configuration files, or tooling contained in this repository.

---

## Responsible Disclosure

We take security seriously. If you discover a vulnerability in this project,  including but not
limited to: remote code execution risks in the web flasher, unsafe handling of user-supplied data,
insecure default configurations, or exposed credentials,  please **do not open a public issue**.

**Report privately:**

| Method | Contact |
|---|---|
| GitHub Security Advisory | [github.com/ICBizLabs/ESP32-DIV-KILAZ/security/advisories/new](https://github.com/ICBizLabs/ESP32-DIV-KILAZ/security/advisories/new) |
| Email | security@icbizlabs.com |

We will acknowledge your report within **72 hours** and aim to release a fix within **14 days**
for critical issues.

---

## What Qualifies as a Security Issue

- XSS, CSRF, or code injection in the web flasher (`tools/flasher.html` or `serve_flasher.py`)
- Unsafe deserialization or path traversal in any Python tooling
- Hardcoded credentials, API keys, or secrets accidentally committed
- Firmware that opens unauthorized network services or backdoors on the flashed device
- Supply-chain risks (compromised dependencies such as `esptool-js`)

## What Does NOT Qualify

- Intended behavior of RF research tools (e.g., beacon generation, BLE advertisement simulation)
  when used in authorized contexts,  these are features, not bugs
- Physical access attacks (the device is research hardware; physical security is the user's
  responsibility)
- Firmware crashes or hangs that do not expose data or provide remote access

---

## Supported Versions

| Version | Supported |
|---|---|
| `v1.0.0-somlok` (latest) | ✅ Active |
| Anything prior | ❌ No support,  please update |

---

## Security Design Notes

### Web Flasher (`tools/flasher.html`)

- Runs entirely in the browser; no backend processes data
- Binary firmware is fetched from `raw.githubusercontent.com` over HTTPS
- Web Serial API requires explicit user gesture (port picker dialog),  no silent access
- The hosted version at `sofia.opensable.com/tools/` is protected by `.htaccess` with
  `Content-Security-Policy`, `X-Frame-Options: DENY`, `Strict-Transport-Security`,
  and `Permissions-Policy`
- `Options -Indexes` prevents directory listing
- All Python scripts, shell scripts, and config files are blocked at the HTTP level

### Firmware

- No credentials are stored in firmware or in this repository
- OTA update fetches from the configured GitHub repository over HTTPS
- Web Control interface (`/tools/` submenu) binds only to the local WiFi AP and does not
  expose services to the internet without user action

---

## Hall of Fame

Responsible disclosures that result in a confirmed fix will be credited here with the
researcher's name or handle, at their preference.

*(none yet)*
