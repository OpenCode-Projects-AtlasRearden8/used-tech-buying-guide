# Wipe It: The Buyer's and Seller's Sides

> Every piece of used tech changes hands at least twice: once with your life still on it, once as someone else's machine. The wipe is how both of you sleep afterward. This chapter gives sellers the leave-clean checklist for every platform, and gives buyers the arguably stranger rule: wipe it again anyway.

## The rule that makes everything else work

**Sign out first, erase second.** On every platform, the wipe only does its whole job if accounts are removed from the device *before* the reset. A reset with accounts still attached leaves Activation Lock, Factory Reset Protection, or a remote-management flag armed - from [Locks, Accounts, and Seed Phrases](04-locks-and-seed-phrases.md). Wipe in the wrong order and the device you sold becomes a brick for the buyer and a paperweight with your name on it for you.

Do it in this order, always:

1. Move off anything you will want later (backup - the boring step that saves people).
2. Sign out of *every* account on the device.
3. Erase / reset to factory state.
4. Verify the device now boots to a clean, account-free setup screen.
5. Remove the device from your remote device lists (Apple's Devices page, Google's devices list, your Microsoft account, Samsung account).

## What a bad wipe actually leaves behind

To know why the checklist is so specific, know what leaks:

- **Photos and "Recently Deleted"** - albums removed from view are not removed from the drive; Photos' trash must be emptied and the device reset, not just tidied.
- **Messages and call logs** that sync back to the cloud even after local deletion - which is why "the messages app is empty" is never proof of anything.
- **Saved Wi-Fi networks** (home and work, plus the passwords that protect them, if the device syncs).
- **Password managers and autofill** - a person's emails, card numbers, and identity, sitting in one app the seller forgot.
- **Notes and files in "hidden" spots**: secure folders, private-note locks, a Photos "hidden" album, documents in a Files/Drive app you never open.
- **Login sessions**: banking, marketplace, and email apps stay "signed in" until signed out *in the app*.
- **Crypto wallets**: wallet apps live in app data, and some quietly offer to "restore" from cloud backups on a fresh device. Empty the wallet, remove the app *and* its data, then reset. (The buyer side of this rule lives in [Locks, Accounts, and Seed Phrases](04-locks-and-seed-phrases.md): accounts first, erase second - wallets included.)
- **Autocorrect and keyboard learning:** embarrassing, harmless, and remarkably tenacious - it is on the checklist for the honest seller.

None of this is exotic. It is why **deleting a photo is not a wipe**, and why every platform has an "erase and reset" item that exists specifically for this moment.

## Sellers: iPhone and iPad

1. **Backup what matters** to a computer or iCloud, and actually restore-test it (restore to your *new* device or a computer; trust, then verify).
2. **Apple Pay / Wallet:** remove cards and passes (Wallet app > each card > "-").
3. **Messages:** leave everything; the reset cleans it - but first make sure pasted photos you need are saved elsewhere.
4. **Sign out of Apple ID:** Settings > [your name] > Sign Out. This is the step that removes Find My and - critically - the step the buyer watched for at the meetup.
5. **Verify on the account side:** account.apple.com > Devices (or iCloud settings) - remove the device from your list.
6. **Erase:** Settings > General > Transfer or Reset iPhone > Erase All Content and Settings. Type in your Apple ID password when asked - being asked again is correct and good.
7. **eSIM:** choose "erase eSIM" during the reset (your carrier plan is on your account; the chip profile is per-device). Pop out the physical SIM.
8. **Verify the finish line:** the device boots to the "Hello" screen and asks nothing of you. If it asks for *your* Apple ID at setup: your sign-out in step 4 did not fully land. Run it again.

## Sellers: Android

1. Backup (Google One or a USB cable to a computer; see what you have before you press anything).
2. **Remove accounts:** Settings > Passwords & accounts > every Google (and Samsung/Xiaomi/etc.) account > Remove. If any account remains at reset, Factory Reset Protection locks the buyer out; for the Samsung variants, also remove the Samsung account.
3. **Wallet apps:** move balances, remove the app, clear its data.
4. **Screen locks:** remove your PIN/pattern (Settings > Lock screen) so nothing hangs on the reset.
5. **Reset:** Settings > System > Reset (or "General management > Reset" on Samsungs) > "Erase all data".
6. **Verify:** the phone arrives at the language-selection screen, and the setup wizard lets you **skip every sign-in**. If it refuses and asks for a previously-synced account, FRP is still armed: run step 2 again with more care.
7. Pop the SIM, tell the truth in the listing about the IMEI status (see the IMEI notes in [chapter 4](04-locks-and-seed-phrases.md)).

## Sellers: Windows laptop

1. Backup your files; download any software you need keys for (and print/keep the license keys somewhere you can find them later).
2. **BitLocker:** suspend or turn it off before the reset (Settings > Privacy & security > Device encryption, or Control Panel > BitLocker Drive Encryption) - or save the recovery key somewhere that survives the reset (your Microsoft account's devices page keeps a copy for you).
3. **Sign out of the Microsoft account** (Settings > Accounts > Your info), then switch to a temporary local account. You need an administrative local account to run the reset.
4. **Reset:** Settings > System > Recovery > Reset this PC > "Remove everything". When the wizard asks, choose **Clean data** / "Fully clean the drive" - slower, but it is the version meant for someone else's hands. If the device was ever managed or enrolled by an IT department, confirm it truly isn't any more; that question and its consequences live in [chapter 4](04-locks-and-seed-phrases.md).
5. **BIOS passwords:** remove any supervisor/administrator password while you are in the BIOS (this buyer asked, per [Test Drives](06-test-drives.md)).
6. **Verify:** the machine boots to the Windows setup/welcome screen and needs nothing from you. If it asks for a Microsoft password to set up, it was not signed out first - run it again.

## Sellers: Mac

1. Backup to an external drive (Time Machine) or iCloud; note down your software licenses.
2. **Sign out of Apple ID:** System Settings > [your name] > Sign Out. Enter the password when asked. When the "keep a copy?" sheet appears, choose to *not* keep anything on the Mac - you already backed up in step 1, and copies defeat the point.
3. Deauthorize iTunes/Music authorizations if you are close to the 5-computer cap (Account > Authorizations > Deauthorize This Computer) - only if it applies to you.
4. **Erase:** System Settings > General > Transfer or Reset > Erase All Content and Settings (Apple-silicon and T2 Macs make this one step). Older Intel Macs: recovery mode (Cmd+R at boot) > Disk Utility > erase the drive > reinstall macOS.
5. **Verify:** the machine boots to the "Hello"/Welcome screen, language picker first, *no password prompts, no FileVault prompts, no old accounts*. Remove the device from your Apple devices list.

## Sellers: Chromebook

1. Sign out of your account.
2. Powerwash: Settings > Advanced > Reset settings > Powerwash.
3. Verify the sign-in screen is clean. If it says "managed" anywhere - the enrollment question from [chapter 4](04-locks-and-seed-phrases.md) - the device is not yours to sell as personal and stays unsold until the organization releases it.

## Sellers: monitor

You would not think a monitor holds anything - and you would be wrong:

- **USB hub ports** may have pairing data, a Bluetooth dongle in a port, or even an SD card inserted and forgotten.
- **Built-in smart apps** (video/streaming monitors) have your streaming-service account sessions; sign out of every one before listing it.
- **Webcam monitors** - check the camera app once, confirm no footage is stored, then factory-reset the monitor's OSD settings from the menu.

## Two wipe-time mistakes that cost the sale

Two wipe-adjacent mistakes happen constantly and cost the sale:

- **"I reset it, but now it asks for my Apple ID / Google account - can I just give you my password and..."** - no. That is a locked device in a buyer's hands. Run the erase again after removing accounts; if it will not accept, troubleshoot the account that remains.
- **"Here's the password, just for now."** Passwords you share during a sale are passwords you gave away. Run the wipe in front of the buyer; sell privacy, not credentials.

## Buyers: wipe again anyway

The device you paid for was wiped - watched by you. Here is why you wipe it again the same evening, gently, without implying anyone lied:

- Resets are human-run. Settings screens sometimes *keep* an account not because someone lied, but because a menu was renamed or a toggle behaved unexpectedly.
- Your own accounts, your own passwords, your own clean slate: whether or not one byte survived, a fresh reset gives you the machine exactly as if it were new from a store.
- It takes ten minutes and you were going to set it up anyway.

So: run the same platform checklist above one more time the same evening - accounts first, erase second, verify the clean setup screen - right after saving the photos you came for and before installing anything personal. Windows machines: reset with "Clean data", or run a clean install from your own USB stick if you got a BitLocker-protected machine. Macs: a second erase loop. Phones and tablets: a second reset, then set up on your own Wi-Fi.

## If something feels haunted after two wipes

Two clean resets should give you a boring machine. If bloatware returns, an old profile shows up, or the device signs into accounts you never added - stop configuring it. Treat it as an unresolved problem: contact the seller first, and if they are unreachable, the platform or refurbisher you used. Only *cold* resets (recovery-installs from external media) come after that, and they are a step for the Revival Guide, not this one.

## Where to go next

- The lock logic that makes wipes matter: [Locks, Accounts, and Seed Phrases](04-locks-and-seed-phrases.md).
- The calm morning-after plan: [After You Buy](11-after-you-buy.md).
- Reviving a machine further (SSD upgrades, Linux installs, local AI): the **Old Laptop Revival Guide** - its "Calm Wipe" chapter covers the *keep-the-machine* case, while this chapter covers the *hand-it-to-someone-else* cases.
