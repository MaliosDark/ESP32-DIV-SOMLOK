# DISCLAIMER & TERMS OF USE
## SomloK Firmware,  ESP32-DIV-SOMLOK Project

**Last updated: 2026**
**Maintained by: MaliosDark (Andryu Schittone)**

---

> **BY DOWNLOADING, CLONING, FLASHING, COMPILING, RUNNING, DISTRIBUTING, OR OTHERWISE
> USING ANY PART OF THIS REPOSITORY, YOU UNCONDITIONALLY AGREE TO ALL TERMS STATED
> IN THIS DOCUMENT. IF YOU DO NOT AGREE, YOU MUST NOT USE THIS SOFTWARE.**

---

## 1. Nature of the Software

SomloK is a **wireless protocol research firmware** for the ESP32-DIV V2 development board.
It includes tools that transmit and receive radio frequency signals across multiple bands
(802.11 WiFi, Bluetooth Low Energy, Sub-GHz ISM bands, 2.4 GHz NRF24, and infrared).

These tools exist for **educational, academic, and authorized security research purposes only**.

---

## 2. Authorized Use Only

You agree that you will **only** use this software:

1. On networks, systems, and devices that **you personally own**, OR
2. On networks, systems, and devices for which you have received **explicit, documented,
   written authorization** from the legal owner prior to any testing activity, OR
3. In **fully isolated laboratory environments** with no possibility of interference with
   third-party systems, OR
4. In the context of an **authorized Capture The Flag (CTF) competition** within its
   defined rules and scope.

**Any use outside of these four categories is strictly prohibited.**

---

## 3. Complete Disclaimer of Liability

TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW:

- **MaliosDark (Andryu Schittone)**, contributors, maintainers, and any individual who has
  submitted code, documentation, or assets to this repository (collectively, "the Authors")
  **accept zero liability** of any kind,  criminal, civil, regulatory, or otherwise,  for
  any harm, damage, loss, or legal consequence arising from the use or misuse of this software.

- The Authors are **not responsible** for and expressly disclaim liability for:
  - Unauthorized access to computer systems or networks
  - Interference with wireless communications
  - Violations of spectrum regulations (FCC, CE, ANATEL, OFCOM, ITU, or any other body)
  - Violations of computer crime laws including but not limited to: the U.S. Computer
    Fraud and Abuse Act (CFAA), the EU Network and Information Security Directive (NIS2),
    Mexico's Ley Federal de Telecomunicaciones y Radiodifusión, or any equivalent law
    in your jurisdiction
  - Privacy violations arising from passive or active monitoring of third-party traffic
  - Any direct, indirect, incidental, special, punitive, or consequential damages
  - Loss of data, equipment damage, or network outages caused by this software
  - Any actions taken by law enforcement or regulatory bodies against a user of this software

- This software is provided **"AS IS"** without warranty of any kind, express or implied,
  including but not limited to the warranties of merchantability, fitness for a particular
  purpose, and non-infringement.

---

## 4. You Are Solely Responsible

By using this software, you acknowledge and agree that:

- **You are the only person responsible** for how you use it.
- You have independently verified that your intended use is legal in your jurisdiction.
- You understand that laws regarding wireless transmission, RF experimentation, network
  scanning, and signal interception vary by country, state, and municipality, and that
  **it is your obligation** to know and comply with all applicable laws.
- The existence of this software in a public repository does **not** imply that any
  particular use of it is legal or ethical.
- The Authors are not your lawyers and nothing in this repository constitutes legal advice.

---

## 5. Specific RF & Wireless Warnings

RF-capable tools in this firmware can:

- Transmit on licensed and unlicensed frequency bands
- Cause interference with medical devices, aviation electronics, emergency communications,
  and other critical infrastructure if misused
- Constitute a criminal offense in many jurisdictions if used without authorization

The Sub-GHz module (CC1101) can operate at frequencies including 315 MHz, 433 MHz, 868 MHz,
and 915 MHz. The NRF24L01+ operates in the 2.4 GHz ISM band. These are regulated spectrum
bands in virtually every country. **You are responsible for complying with all applicable
spectrum regulations.**

---

## 6. No Endorsement of Illegal Activity

The inclusion of any tool in this firmware does not constitute endorsement, encouragement,
or authorization to use that tool for any illegal purpose. Descriptive names like
"Deauth Research", "Disassociation Research", "HID Payload Research", or "Interference Lab"
are technical descriptions of protocol interactions for educational purposes only.

---

## 7. Indemnification

You agree to **indemnify, defend, and hold harmless** MaliosDark and all Authors from and
against any and all claims, liabilities, damages, losses, costs, and expenses (including
reasonable legal fees) arising from or related to:

- Your use or misuse of this software
- Your violation of any applicable law or regulation
- Your violation of any third party's rights
- Any claim that your use of this software caused harm to a third party

---

## 8. Modifications and Derivatives

If you fork, modify, or distribute a derivative of this software, you must:

- Include this DISCLAIMER.md in its entirety in your distribution
- Make clear to your users that the software contains RF research capabilities
- Not remove or alter the warnings in this document
- Include a statement of what changes you made relative to the original

You may not represent a modified version as the original SomloK firmware.

---

## 9. Governing Law & Jurisdiction

These terms shall be interpreted in accordance with internationally recognized principles
of software licensing law. Where a specific jurisdiction must be named for purposes of
dispute resolution, the parties agree to submit to the jurisdiction of applicable courts
in the country of the repository owner's principal place of business.

If any provision of this disclaimer is found unenforceable in a given jurisdiction, the
remaining provisions shall continue in full force and effect.

---

## 10. Acknowledgment

By proceeding to use any part of this software, you confirm that:

- [ ] You are at least 18 years of age, or have the consent of a legal guardian
- [ ] You have read and understood this entire document
- [ ] You agree to use this software only in authorized contexts
- [ ] You accept sole responsibility for your actions
- [ ] You will not hold the Authors liable for any outcome of your use of this software

---

*This disclaimer was written to be comprehensive, not to be intimidating. SomloK is a
legitimate research tool used by security professionals, educators, and hardware enthusiasts
worldwide. Use it responsibly, learn from it, and stay legal.*
