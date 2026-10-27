# Locks, Accounts, and Seed Phrases

> This is the chapter that keeps you from buying a beautiful brick. Every locked-device horror story ends the same way: someone paid for a device, tried to set it up, and a stranger's account bar appeared. Read this one twice. It costs nothing and saves whole purchases.

## The one rule

**You are not buying the device. You are buying the ability to use the device.** That ability lives in the seller's accounts, not in the seller's pocket. Until the device sets up fresh - on a "Hello" screen, or a clean install, signed into nobody - the deal is not real yet.

## Activation Lock (Apple: iPhone, iPad, Mac)

Activation Lock ties any erased Apple device to the last Apple ID that had Find My enabled. Wipe it while still signed in, and the next setup demands that owner's password. Forever. With no back door for buyers.

**The buyer's ritual - do all of it in front of you, at the meetup, before paying:**

- [ ] Seller opens Settings, taps their name at the top - show me the account screen.
- [ ] Seller scrolls and taps **Sign Out**, and enters *their* Apple ID password (the screen will say it's disabling Find My).
- [ ] Then Settings > General > Transfer or Reset iPhone (or "Erase All Content and Settings" on Mac: system settings > erase) - run the erase with you watching.
- [ ] The device finishes on the **Hello / "Welcome to iPhone"** screen.
- [ ] You begin setup yourself: choose language, connect Wi-Fi (your hotspot), and the "hello" flow proceeds **without ever asking for the old owner's Apple ID**. If any screen asks you to enter *their* credentials: the sale is off. Politely return it.

Notes that protect you:

- A **factory reset alone is not enough.** The reset must come *after* the sign-out above, or Activation Lock survives the erase. Sellers get this wrong innocently all the time - which is why you watch, not ask.
- If the seller "can't remember the Apple ID password," Apple can help *them* recover it at their own pace. You can wait days or walk. Device will not be bricked less by your optimism.
- Macs: same spirit. Watch them sign out of Apple ID (System Settings), then erase, then get to the second user-creation screen with no old-account interruptions. FileVault-enabled Macs that reset without sign-out still boot to old-owner prompts on the setup page - the demo proves the point.
- The old owner should also remove the device from their device list (account.apple.com > Devices). That's their housekeeping to do, but you can remind them kindly.

## Factory Reset Protection (Google: Android phones and tablets)

Same concept, Google's flavor. If any Google account was on the phone when it was factory reset, the setup wizard insists you sign back in with *that exact account*. No password, no phone.

**The buyer's ritual:**

- [ ] Seller opens Settings and removes **every Google account** (Settings > Passwords & accounts > tap each > Remove). No residual accounts - "work profile" panels count.
- [ ] Samsung devices: also remove the **Samsung account** and turn off Samsung's "Reactivate Lock" / Find My Mobile.
- [ ] Seller runs the **factory reset** (Settings > System > Reset, or Samsung: Settings > General management > Reset).
- [ ] You complete the setup wizard on the spot: skip/decline every sign-in. If the wizard *refuses* to let you skip a previously-synced Google account: FRP is still armed. That device goes back; deal off.

Quick sanity check phrase for sellers: "Set it to the sign-in-free setup screen, and I'll finish the rest at home." Sellers who have done this before nod and do exactly that.

## The Chromebook trap (enterprise enrollment)

Schools and companies buy Chromebooks by the fleet, and fleet Chromebooks stay managed forever until the organization deprovisions them. Powerwash does **not** remove enrollment; the machine relocks to the school/company console at the next sign-in.

- If the sign-in screen or Settings anywhere says "managed", "enrolled by", or shows a school/company domain - **pass**, unless the seller is that organization or shows genuine deprovisioning. Surplus fleet devices are everywhere and mostly cheap for a very good reason. See Chromebook enterprise enrollment in the [Glossary](glossary.md#chromebook-enterprise-enrollment).

## Windows laptops (BitLocker and accounts)

Windows is forgiving about *locking*, but punishing about *data and encryption*:

- **BitLocker:** business laptops often ship with the drive encrypted. If a seller resets the PC while BitLocker is on and they never saved the recovery key, the erase stalls and the drive needs a full clean install from a USB stick - which is fine, but it needs to be done by someone with the time and the stick: usually you, at home (see [Wipe It](09-wipe-it.md)). The clean version: the seller should suspend or disable BitLocker before selling, or you should plan the install yourself.
- **Accounts:** Windows has no forever-lock like iCloud, but you still want the seller signed out of their Microsoft account and OneDrive, reset to a clean desktop, and left alone until you set up your own account - which should happen at home, not in the parking lot.
- **BIOS passwords** (supervisor/administrator passwords on business laptops) are a real and permanent lock: the seller removes them, or you pass. Ask plainly at the meetup - "any BIOS or admin passwords?" - and if the answer is "I don't know", watch one reboot into the BIOS together before deciding.

## And now: seed phrases

Devices that held crypto wallets carry one extra danger that has nothing to do with screen resolution:

1. **Never type a seed phrase into a used device.** Not to "check the wallet", not to "prove it's real", not to "verify it's genuine": you never enter seed words because a stranger asks, into anything, anywhere, ever. A seed phrase typed at a stranger's request is the exact scenario scam scripts depend on.
2. **Never accept paper or photos with seed words as part of a purchase.** That is step one of wallet-theft folklore: the person who "donated" the words kept a copy, and anything you do in that wallet is watched by them. One rule to burn into your memory: **a seed phrase you did not generate is a seed phrase that is already compromised.**
3. **Sellers: empty and uninstall before the meetup.** Move funds, remove the wallet app *and its data* (the wallet preferences you never intend to check again), factory reset, then verify after the reset that no wallet app or accounts remain.
4. **If you ever receive a device with a wallet installed or words attached:** treat all of it as hot. Wipe the device immediately (yours has different rules - see [Wipe It](09-wipe-it.md)); never fund the pre-existing wallet.

The calm one-liner: **seed words are master keys; a used device carries other people's locks until it's wiped; and the only seed phrase you will ever type is one you wrote down yourself.**

## The stolen-device question (IMEI, and belief)

Phones can be reported lost or stolen after a sale. A reported device gets its IMEI blacklisted: it works on Wi-Fi and stops being a phone. (Tablets have no IMEI; laptops do not either. This section is phones specifically.)

- **Ask and hear the answer:** Settings > About phone shows the IMEI - the honest seller reads it straight off, confirms it is paid off, and confirms it has never been reported lost or stolen. Sellers with clean devices answer without hesitating.
- Optional and worth ten minutes when the price is high: use any public IMEI-checking website from your phone at the meetup (or at home before you go). Free checks tell you if the model exists, is locked to a carrier, or is blacklisted. This guide links none of them on purpose - pick any well-known one yourself at your own pace.
- Receipts help: "do you still have the box or a receipt?" is not an insult. It is the kind of question a friend asks a friend.

## Walking-away language that stays kind

You will use these words. Practicing them tonight makes them faster at the meetup:

- "Thank you - would you be able to sign out of iCloud in front of me? If not, I'll pass today and look elsewhere."
- "The reset needs to happen before I pay. Happy to stand here while it does."
- "If this turns out to be a bit much for today, no problem - I hope it goes to a good home."

Notice what is missing from all three: accusation. The checks are *rules you follow*, not tests the seller failed. Most sellers will complete every step happily. The rare ones who bristle are telling you something for free.

## Where to go next

- The meetup order of operations, locks included: [Test Drives](06-test-drives.md).
- Definitions for everything bolded: the [Glossary](glossary.md) - start at Activation Lock, BitLocker, FRP, IMEI.
- When even a perfect wipe is not enough to make today's device worth it: [New or Used](10-new-or-used.md).
