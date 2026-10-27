# Glossary

> Plain-English definitions, in the order the guide actually uses them. Written to be read at a meetup on a phone, one entry at a time.

## Hardware and panels

### AMOLED / OLED

Screen technology where every pixel lights itself. Phones and some tablets use it. The upside: deep blacks and thin panels. The downside: burn-in - see [Burn-in](#burn-in).

### Backlight bleed

Glow around the edges of a screen, visible on dark backgrounds. Some bleed is normal on laptops (the backlight sits behind liquid-crystal panels); heavy blotchy patches are a manufacturing lottery, and price reductions are for the patchy ones.

### BIOS password

A password stored by the laptop itself, below the operating system. It survives any reset and makes a machine unusable for the next owner. Sellers remove it (in the BIOS settings); buyers ask about it at the meetup and watch it happen.

### Burn-in

A permanent ghost image on OLED screens - keyboard layouts, status bars, app layouts left on-screen for too long. Not fixable, gets worse over years, and worth more on the price sheet than anywhere else.

### Cycle count

How many times a battery has been discharged the equivalent of one full charge (half drained twice counts as one). Modern MacBook batteries are commonly rated for 1,000 cycles; many phone batteries live 500-700 before sinking below 80%. See [Battery health](#battery-health).

### Dead pixel

A pixel that never lights: black on every background. Unfixable without replacing the panel. One or two in a corner of an older machine is a negotiable discount; dead pixels in the bright center of the field are a walk-away.

### Design capacity / FULL CHARGE capacity

Windows' battery-report pair of numbers. Design = what the battery held new; full charge = what it holds today. Full divided by design is the battery health percentage. See [Battery Health](02-battery-health.md).

### Digitizer

The touch-sensitive layer of a phone or tablet screen. Cracked glass with a working digitizer is a cheap screen job; dead digitizer zones (touch that doesn't register in one strip) mean the whole assembly is tired.

### eMMC / SSD / HDD

Storage flavors, oldest to newest: eMMC (a slow little chip, common on very cheap laptops), HDD (spinning platters, slow and bouncy), SSD (fast, modern, the standard). Storage type is easily checked on the About screen, and a "HDD half-broken forever" story is less scary than an SSD claim that will not boot.

### IPS / LCD

The standard non-OLED screen family: colors stay stable at wide angles and there is no burn-in, but blacks glow a little (that is Backlight bleed territory, above). Almost every laptop screen is LCD/IPS.

### PWM flicker

"Dimming" screens (esp. phones at low brightness) switch pixels on and off faster than the eye usually sees. Some people see it anyway and it tires them out. Test: watch a monitor at its lowest brightness for a minute and decide how it sits with you.

### Refresh rate

How many times per second a display redraws: 60Hz standard, 120Hz-165Hz in gaming panels. A "144Hz" panel running at 60 looks instantly duller scrolling a page. Set the OS refresh rate in the display settings at the meetup.

### Stuck pixel

A pixel stuck on one color (or white). Different from a dead pixel; sometimes fixes with "pixel-cycling" software, usually doesn't. Same price treatment either way.

### Swollen battery

A battery gone round: lift under a trackpad, keys pushing up, back cover bulging, a visibly curved phone frame. A hazard and a walk-away, always. The fix is a battery shop, and the seller knows one now.

## Batteries

### Battery health

How much capacity a battery still holds versus when it was new. Phones expose it in Settings (Maximum Capacity %); Macs in System Report; Windows in the `powercfg /batteryreport`. The single most price-moving number in used tech, which is why it owns a whole chapter: [Battery Health](02-battery-health.md).

## Accounts, locks, and security

### Activation Lock

Apple's "this iPad is linked to Joe" lock. It survives factory resets and gates the setup screen until the linked Apple ID's password is entered. Sellers clear it by signing out (Settings > [name] > Sign Out) *then* erasing. Buyers verify with the [Hello-screen test](04-locks-and-seed-phrases.md); sellers who cannot clear it are selling a brick.

### BitLocker

Windows disk encryption. Great for protecting *your* data before selling: the seller disables or suspends it before reset, or saves the recovery key. A BitLocker-protected machine without its key needs a clean install from USB.

### Blacklist / Bad ESN

A phone's IMEI is registered lost/stolen or unpaid, and carriers refuse it: WiFi works, being-a-phone doesn't. Permanent and unfixable. Ask the IMEI question before you drive anywhere.

### Chromebook enterprise enrollment

A Chromebook registered to a school or company console. Powerwash doesn't clear it; the next sign-in re-locks it. Only the owning organization can deprovision a device - which is why surplus "school Chromebooks" are cheap forever and mostly not worth buying.

### FRP (Factory Reset Protection)

Google's version of Activation Lock: a factory reset on a device with Google accounts leaves the setup wizard demanding one of those accounts. Sellers remove every account *first*, then reset; buyers skip every sign-in during setup to verify.

### Find My

Apple's locate/lock service. Having it on is what keeps Activation Lock armed, which is why the seller's sign-out (which disables Find My) is the single step a buyer should insist on watching.

### IMEI

A phone's worldwide serial number, visible in Settings > About. Report a lost/stolen device to the carrier and this number gets blacklisted. Photo of the IMEI goes in your purchase records, always.

### Seed phrase

The 12-24 words that are the master key of a crypto wallet. Anyone with the words controls the money. Type them only into a wallet you set up yourself, never because a stranger asked, and treat seed words handed to you as already compromised. See the full rules in [Locks, Accounts, and Seed Phrases](04-locks-and-seed-phrases.md).

## Money and markets

### Comps

Recent *sold* prices for the same model, storage, and condition - the honest benchmark behind every offer in [Fair Prices](05-fair-prices.md). Sold listings, not asking prices: asks are hopes, sales are facts.

### Certified refurbished / open-box

Manufacturer-refurbished devices are rebuilt, tested, and warrantied (Apple's own program includes a new battery and shell). Open-box means retail returns, often unopened. Both are the middle paths between private-used and new: see [New or Used](10-new-or-used.md).

### OBO

"Or best offer": the listing's built-in invitation to negotiate. It is permission, not a trick - respond with your comps-anchored number from [Negotiation Scripts](07-negotiation-scripts.md).

## Where to go next

Back to the top: [Read This First](00-read-this-first.md). Every chapter, on one page: the site's [Print all](book.html) page.
