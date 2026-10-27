# Battery Health: Check It Before You Pay

> The battery is the most expensive thing you cannot see in a listing photo. On phones and older laptops, a worn battery can turn a "great deal" into a repair bill bigger than the discount. Check the battery the way you would check a car: not by color, by mileage.

## Why battery health is the deal

- **It is the only major part that wears on a schedule.** Screens, chips, and ports can be fine for a decade. Batteries are consumables: every full charge cycle shaves a little capacity off.
- **Replacement cost is real money.** A phone battery service runs roughly $70-130 at a shop (often less at a market stall, more through a manufacturer service center). A laptop battery runs $40-160 plus labor depending on whether it is screwed in or glued. A tablet sits between. Add that number to every price.
- **Low capacity is not just runtime.** A battery below ~80% causes stuttering under load (thermal throttling kicks in to protect old cells) and unexpected shutdown as the percentage slides on cold mornings.
- **Battery numbers are checkable in minutes, in front of you.** Every modern platform exposes battery health somewhere a human can show you. A seller who cannot or will not show it is choosing not to - that tells you plenty.

## Reading the numbers

Two figures matter, and they are different things:

| Figure | What it is | What "good" looks like |
| --- | --- | --- |
| **Maximum Capacity** (%) | Full-charge capacity as a share of what the cell held when new | 85%+ for a 1-2 year old phone; 80%+ acceptable on a 3-year-old laptop; below 75% is budget-replacment territory |
| **Cycle count** | How many times it has been discharged the equivalent of one full battery | Modern phones: 400-600 cycles before meaningful wear; modern MacBook batteries are commonly rated for 1,000 cycles; many Windows laptops give ratings between 300-800 |

The two tell you different stories. Capacity tells you what is left **today**; cycles tell you how **fast** it is getting there. A rare 3-year-old phone at 90% is better news than a one-owner phone at 78% - and a laptop at 82% with 260 cycles is aging politely, while 82% at 700 cycles is sagging.

Rules of thumb for capacity:

| Device age | Comfortable | Negotiate down | Budget a replacement |
| --- | --- | --- | --- |
| Under 1 year | 92%+ | 88-92% | <88% |
| 1-2 years | 88%+ | 80-88% | <80% |
| 2-3 years | 82%+ | 75-82% | <75% |
| 3-5 years | 75%+ | 65-75% | <65% |
| 5+ years | 70%+ | 60-70% | <60% |

These are starting lines, not sales pitches: a 4-year-old iPad at 91% is a perfectly good buy. The point of the bands is to argue with, not obey.

## iPhone and iPad

On modern iPhones and iPads (iPadOS 14+), battery health is one screen away.

- **Path:** Settings > Battery > Battery Health & Charging. Read **Maximum Capacity** and whatever the status line says underneath it.
- **Words matter on this screen.** "Peak Performance Capability" is fine. If it says the battery "significantly degraded" or a service message appears, Apple already told you what the repair conversation costs.
- **"Service" under Battery Health** = old cells, expensive day. Price the repair in or walk.
- **Cycle count is not shown** on iPhones, but the percentage plus the model's age gets you close enough for a buying decision.
- Third-party-repaired phones can show odd readings: if the device says it "confirms genuine part" is not available, ask when the battery was replaced, and expect it to age like a mystery part (value accordingly).
- Ask for the **live** screen at the meetup, not a screenshot. Screenshots get made in photo editors. If the meetup is a no-go, at least make them send it as a video with them swiping somewhere mid-clip.

## Android phones and tablets

There is no single universal battery-health screen on Android, which is why the in-person check matters more. In rough order of how useful each method is:

1. **The maker's own diagnostic app.** Samsung phones: Samsung Members app > Support > Interactive checks > Battery (shows "Life" as Good/Normal/Weak, not a percentage). Some Sony, Motorola, and OnePlus builds expose battery info in Settings > Battery, or via Device Care / Phone Care screens.
2. **The dialer code (works on some models):** open the phone app and type `*#*#4636#*#*` - if a menu appears, tap Battery information. Many modern phones have removed this; silence does not mean a bad battery.
3. **The live behavior test** (the one that is hard to fake at a meetup):
   - Plug a healthy USB-C charger into the seller's device with the seller watching. A healthy phone gains about 1% per minute in the charge range, give or take. A dying one crawls or swings.
   - Watch the percentage slide while you talk for five minutes with the screen on. Numbers that move fast and far are a story about cells, not location.
4. **Ask the age question.** "How long have you had it, and is the original battery?" A $20 part in last year is not a dealbreaker if the price reflects it.

Tablets age batteries slower than phones (less drain per session), so you can apply the same thresholds a little gently: an 82% tablet serves a couch reader just fine.

## Laptops: macOS

Mac laptops report everything through the system itself:

1. Press and open **About This Mac > System Report (More Info / System Report)**, or hold Option while the Apple menu is open and choose System Information.
2. Choose **Power** from the left list.
3. Read **Cycle Count** and **Condition**. "Condition: Normal" is what you want; "Service Recommended"/"Service Battery" is the repair flag.

From Terminal if you prefer one command:

```text
system_profiler SPPowerDataType | grep -i -A1 cycle
```

Modern MacBook batteries are typically rated for 1,000 full cycles. A 3-year-old MacBook Air at 220 cycles is a cautious owner (good sign); 800 cycles means the battery is closer to the end of its rating.

Bonus checks on a Mac:

- Charge to 100% only if you insist; the right question is whether it drains slowly when unplugged. At the meetup, ask to unplug for ten minutes while you test other things; a battery that drops fast is answering everything.
- If the battery is swollen (see below), do not buy, and advise the seller gently to not keep charging it.

## Laptops: Windows

Windows gives a full battery report with two commands and no admin rights:

```text
powercfg /batteryreport
```

1. This writes `battery report.html` to the user profile folder (the path prints right below). Have the seller run it and open the report.
2. In the report, find **Installed batteries**: read **DESIGN CAPACITY** and **FULL CHARGE CAPACITY**.
3. Divide: FULL CHARGE / DESIGN = the health percentage. 80% or better is comfortable for most laptops; below 70% start pricing in a replacement.

The report also shows recent discharge history - very useful if the seller used the laptop nightly and let it age visibly. Also glance at **CYCLE COUNT** where the report includes it. And if the graph shows odd sawtooth jumps, ask whether the battery was replaced (the answer, again, gets priced in).

Alternatively, some Windows laptops (Dell, Lenovo, HP business lines) have built-in diagnostics in their support app or BIOS; the powercfg report is the universal shortcut.

## Laptops: Linux and Chromebooks

- Linux: run `upower -i /org/freedesktop/UPower/devices/battery_BAT0` and read `capacity` and `energy-full` vs `energy-full-design` and `cycle count`.
- Chromebook: type `chrome://diagnostics` into the browser address bar and open the **Battery** section - it shows capacity and health in plain numbers.
- For more about reviving a machine that keeps showing Linux, the **Old Laptop Revival Guide** picks up where this chapter's checklist ends.

## The swollen battery (stop reading, start walking)

A lithium battery that has swelled is not a discount, it is a hazard:

- **How to see it:** a trackpad that sits proud of the metal, keys that bulge, a chassis that wobbles on a flat table, a back cover lifting, a phone screen pushing away from the frame, a tablet bending slightly.
- **What not to do:** do not press the bulge to "see how bad". Do not charge the device. Do not puncture, squeeze, or ship it raw.
- **What to do:** tell the seller *calmly* that it has to stop being charged today, that a battery shop will take it for recycling, and end the deal. If the seller is a friend, find a battery drop-off - most repair shops and electronics retailers take swollen cells at no cost.

If a device passes the battery checks but the seller mentions "it got warm once or twice" - lean on Guide 6's heat test: run it at full brightness for ten minutes doing real work, not idle.

## Where to go next

- Screen testing, the other 10-minute check: [Screen Checks](03-screen-checks.md).
- Price the battery wear into an offer: [Fair Prices](05-fair-prices.md).
- Inspecting a specific device? The checklists live in the Worksheets folder: [Laptop Worksheet](worksheets/laptop-worksheet.md), [Phone Worksheet](worksheets/phone-worksheet.md), [Tablet Worksheet](worksheets/tablet-worksheet.md), and [Monitor Worksheet](worksheets/monitor-worksheet.md) (monitors have no battery - their own checks are different).
