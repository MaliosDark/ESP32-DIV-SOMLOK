## SUB 32 Protocol Decoder

**Purpose:**
Receives and decodes many RCSwitch-compatible fixed-code SubGHz remotes. It shows the detected value, bit length, protocol number, and a best-effort classification for common fixed-code families such as PT2262 and EV1527 class devices.

**How to use:**
- Enter from Full Suite or Tool Catalog as "SUB 32 Protocol Decoder".
- Use UP/DOWN to change frequency band (315, 433, 868, 915 MHz).
- Transmit with a nearby remote and watch the live code, bit length, protocol ID, and RSSI.
- Press SELECT to exit.

**Tips:**
- Place the device near a remote or sensor and press a button to see the code.
- This tool is best for fixed-code remotes and basic sensors.
- Rolling-code systems are not decoded here.

---
## SUB 31 Spectrum Analyzer

**Purpose:**
Visualizes SubGHz spectrum activity as a live waterfall/heatmap. Each column is a frequency, each row is a time slice, and color shows RSSI (signal strength). Useful for finding active bands, jammers, or unknown signals.

**How to use:**
- Enter from Full Suite or Tool Catalog as "SUB 31 Spectrum Analyzer".
- The display shows a scrolling waterfall: X axis = frequency, Y axis = time, color = signal strength.
- Green = strong, yellow = medium, red = weak.
- Press SELECT to exit.

**Tips:**
- Place the device near sources of SubGHz activity to see live changes.
- Use this tool to identify busy or quiet bands before jamming, replay, or protocol analysis.

**Note:**
This is a visual tool only; no demodulation or decoding is performed.

---
## SYS 11 File Manager

**Purpose:**
Provides an on-device SD browser for the main SomloK storage areas: `/captures`, `/subghz`, `/ir`, `/ducky`, `/logs`, and `/config`. It shows file type, size, and supports guarded deletion without removing the SD card.

**How to use:**
- Open it from `Tools > File Manager` or from Full Suite as `SYS 11 File Manager`.
- Use UP/DOWN to move through entries.
- Use SELECT or RIGHT to open a directory.
- Use LEFT to go back, or exit when already at the root.
- On a file, press RIGHT once to arm deletion and RIGHT again within the confirmation window to delete it.

**Tips:**
- Use this page to clean up captures, SubGHz exports, IR files, Ducky payloads, and logs directly from the device.
- Deletion is only enabled for files, not directories.

---
## SYS 12 Signal Library

**Purpose:**
Provides a unified browser for compatible IR and SubGHz files anywhere in the main SD storage areas. It validates each file against the real SomloK storage formats and then imports it into the correct library.

**How to use:**
- Open it from `Tools > Signal Library` or from Full Suite as `SYS 12 Signal Library`.
- Use UP/DOWN to browse all compatible entries found in `/captures`, `/subghz`, `/ir`, `/ducky`, `/logs`, and `/config`.
- Entries marked with `*` are already in the canonical library.
- Press SELECT or RIGHT to import the selected file.
- IR files are copied into `/ir` with the expected `ir_XXXX.bin` format.
- SubGHz exports are loaded into the active current bank and archived into `/subghz` when needed.

**Tips:**
- Use this after uploading captures through Web Control or copying files onto the SD card manually.
- Imported IR files become immediately visible in `IR > Saved Profile`.
- Imported SubGHz banks become available through `SubGHz > Saved Profile`.

---
## SYS 13 Web Control

**Purpose:**
Starts a dedicated access point and serves a headless management dashboard for live device status, screen context, theme/brightness control, SD upload, and SD file deletion.

**How to use:**
- Open it from `Tools > Web Control` or from Full Suite as `SYS 13 Web Control`.
- Connect a phone or laptop to the access point `SomloK-Control` using password `somlok123`.
- Browse to the IP shown on the device screen.
- Use the web page to view live status, adjust theme and brightness, upload files into the main SD folders, and delete files.
- Press SELECT on the device to stop the service and exit.

**Tips:**
- The dashboard shows the active screen context so you can confirm what the device is doing without touching the TFT.
- Upload IR or SubGHz files, then use `Signal Library` to validate and import them into the canonical libraries.

---
## SYS 14 RF Hot/Cold

**Purpose:**
Provides proximity guidance for two different RF hunting workflows: live SubGHz RSSI using the CC1101 and strongest 2.4GHz beacon strength using nearby WiFi activity.

**How to use:**
- Open it from `Tools > RF Hot/Cold` or from Full Suite as `SYS 14 RF Hot/Cold`.
- Use LEFT/RIGHT to switch between `SubGHz` and `2.4GHz` modes.
- In `SubGHz` mode, use UP/DOWN to cycle through 315, 433.92, 868.35, and 915 MHz.
- In `2.4GHz` mode, use UP or DOWN to force a fresh WiFi scan.
- Follow the heat meter and guidance text to move toward stronger signals.

**Tips:**
- For SubGHz, rely on the smoothed RSSI line instead of single spikes.
- For 2.4GHz, this tool uses the strongest WiFi beacon as a practical proximity proxy.

---
## Theme Picker And Settings

**Purpose:**
The main `Setting` screen already includes a live theme picker, brightness slider, NeoPixel toggle, and auto-scan control. Theme changes are applied immediately and saved persistently. The NeoPixel toggle now drives the 4 WS2812 LEDs above the display.

**How to use:**
- Open `Setting` from the main menu.
- Use LEFT/RIGHT or touch to cycle through all available themes.
- Adjust brightness directly on the same page.
- Save changes from the footer to persist them across reboots.

**Available themes:**
- Dark
- Light
- AMOLED
- Ice Lab
- Signal Amber
- Abyss Bloom

**Original theme:**
- `Abyss Bloom` is a custom reimagined palette built specifically for this firmware update, mixing deep teal shadows, warm coral icons, and pale mint accents for a more atmospheric look than the stock styles.

**NeoPixel indicator meanings:**
- The 4 top WS2812 LEDs stay off while no tool is actively running.
- `WiFi` tools use a blue sweeping pattern.
- `BLE` tools use a cyan and magenta pulse.
- `2.4GHz` tools use a fast green scan pattern.
- `SubGHz` tools use an amber scanner-style sweep.
- `IR` tools use a red pulse.
- `Ducky` tools use a stepped purple fill.
- `Settings` and `System` pages use a soft white and green status pattern.
- `About` uses a warm white glow.

**Button flash meanings:**
- `UP` flashes light blue.
- `LEFT` flashes amber.
- `RIGHT` flashes magenta.
- `DOWN` flashes green.
- `SELECT` flashes white.

**Notes:**
- These LEDs are activity indicators for the 4 top NeoPixels only, not the fixed side indicator LEDs on the board.
- Colors are intended as fast visual hints for tool category and button input, not as warning levels.

---
# SomloK Firmware

SomloK is a unified ESP32-S3 wireless research firmware build.

## Identity

- Project: SomloK
- Developer: Malios Dark
- Version: v1.0.0-somlok
- Reference repositories:
   - cifertech/ESP32-DIV
   - JesseCHale/ESP32-DIV
   - ICBizLabs/ESP32-DIV-KILAZ

## Build And Flash

Preferred build command:

```bash
./tools/build_somlok.sh
```

This script applies the validated `TFT_eSPI` setup from `config/tftespi/User_Setup.ESP32_DIV_V2_ILI9341.h` before compiling. If your `TFT_eSPI` library lives outside the default Arduino sketchbook location, set `TFT_ESPI_LIBRARY_DIR` or `TFT_ESPI_USER_SETUP_DEST` before running the script.

Equivalent `arduino-cli` compile command after the setup has been applied:

```bash
arduino-cli compile \
   --fqbn esp32:esp32:esp32s3:FlashSize=16M,PartitionScheme=app3M_fat9M_16MB,USBMode=default,CDCOnBoot=cdc \
   --build-property compiler.c.elf.extra_flags="-Wl,--allow-multiple-definition" \
   --export-binaries \
   /home/nexland/ESP32-DIV-KILAZ/firmware/SomloK
```

Validated upload command:

```bash
arduino-cli upload \
   -p /dev/ttyACM0 \
   --fqbn esp32:esp32:esp32s3:FlashSize=16M,PartitionScheme=app3M_fat9M_16MB,USBMode=default,CDCOnBoot=cdc \
   /home/nexland/ESP32-DIV-KILAZ/firmware/SomloK
```

For the white-screen recovery summary and the validated display pin map, see `docs/esp32-div-v2-display-setup.md` in the repository root.

   Latest validated memory footprint:

   - Flash: `1449345 bytes (46%)`
   - Global RAM: `111276 bytes (33%)`

## Full Tool Catalog

   The complete SomloK catalog currently contains 93 tools.

### WiFi Tools (19)

1. Packet Monitor
2. Beacon Spammer
3. WiFi Deauther
4. Deauth Detector
5. WiFi Scanner
6. Captive Portal
7. Evil Twin Detect
8. Probe Sniffer
9. Hidden AP Detect
10. Rogue AP Scanner
11. Channel Analyzer
12. EAPOL Capture
13. PMKID Capture
14. Karma Attack
15. WiFi Geiger
16. Pwnagotchi Detect
17. Probe Flood
18. Ping Scanner
19. Station Tracker

### Bluetooth Tools (16)

1. BLE Jammer
2. BLE Spoofer
3. Sour Apple
4. Sniffer
5. BLE Scanner
6. Skimmer Detect
7. Camera Finder
8. GATT Explorer
9. Android Spam
10. Beacon Cloner
11. BLE Fuzzer
12. Flipper Detect
13. Flipper Spam
14. AirTag Spoof
15. Flock Detect
16. BLE Rubber Ducky

### 2.4GHz Tools (8)

1. Scanner
2. 2.4GHz Analyzer
3. Tracker Detector
4. Proto Kill
5. Drone Detector
6. MouseJack Detect
7. WiFi Cam Detect
8. Multi-Channel 24

### IR Tools (9)

1. IR Record
2. Saved Profile
3. TV-B-Gone
4. HVAC Controller
5. IR Brute Force
6. Universal Remote
7. Protocol Analyzer
8. Macro Sequencer
9. Flipper Import

### SubGHz Tools (27)

1. Replay Attack
2. SubGHz Jammer
3. Saved Profile
4. Freq Analyzer
5. TPMS Decoder
6. Weather Decoder
7. Smart Meter
8. Relay Detector
9. Bug Sweeper
10. Bruteforce
11. ProtoView
12. Rolling Flaws
13. Tesla Charge Port
14. POCSAG Decoder
15. Genie Recorder
16. RAW Recorder
17. Freq Scanner
18. Garage Protocols
19. Car Key Analyzer
20. Doorbell Trigger
21. Doorbell Brute
22. FZ Analyzer
23. Security Sensors
24. Multi-Freq Scanner
25. Flipper File
26. Spectrum Analyzer
27. Protocol Decoder

### System Tools And Settings (14)

1. Serial Monitor
2. Update Firmware
3. Button Checker
4. Brightness
5. Screen Timeout
6. NeoPixel Control
7. SubGHz Region
8. Device Info
9. WiFi Setup
10. License
11. File Manager
12. Signal Library
13. Web Control
14. RF Hot/Cold

## Hardware Target

- ESP32-S3
- 16MB flash
- TFT display
- Touch controller
- CC1101
- NRF24
- SD card

## Legal

Use this firmware only on systems and radio environments where you have explicit authorization.
