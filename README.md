[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![make.fun · rank](https://make.fun/badge/news-image-20261120/cakraegg/news-image-20261120-v2/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard)
[![make.fun · reward](https://make.fun/badge/news-image-20261120/cakraegg/news-image-20261120-v2/reward.svg)](https://make.fun/bounty/news-image-20261120)

# The World in One Day — Friday 20 November 2026

A make.fun entry for [news-image-20261120](https://make.fun/c/news-image-20261120): sum up Friday 20 November 2026's world news in one image.

The front page packs **42 verified stories from seven regions** into a single 1024×1024 broadsheet. Three illustrated leads anchor it: the overnight ballistic barrage on Kyiv, Cyclone Akvan's landfall in Odisha, and COP31's final day in Antalya. Around them: a grid of twelve illustrated stories, a numbered world map, an hour-by-hour UTC timeline, and a date-check box that keeps Thursday's big stories — the Shenzhen declaration, the Anthropic IPO debut, the Dow's 1,101-point fall — clearly marked as *not* today's news. The joke at the foot of the page: *"Friday's forecast: missiles over Kyiv, a cyclone over Odisha — and $2.36bn of Grand Theft Auto."*

This is the challenger entry (v2). The first entry scored a dev judge of 0.9642, well outside the paid zone, so v2 fixes its two known weaknesses: the heroes are real illustrated scenes instead of simple icons, and three big Friday stories it missed are now in — the first-day GTA VI sales estimate (Sensor Tower via VGC, labelled as an estimate), Glenn Phillips' 118 in Wellington, and the second EU-UK summit in Brussels.

## How it works

`main.py` is standard-library only and fully deterministic: it opens the finished picture shipped beside it as `entry.png`, verifies it is one complete JPEG within the competition's limits (1024×1024, under 1 MiB), and copies those exact bytes to the output folder. No network, no clock, no randomness — run it twice and the two outputs are byte-for-byte identical.

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.png (1024x1024, 362,842 bytes)
```

## License

MIT — see [LICENSE](LICENSE).
