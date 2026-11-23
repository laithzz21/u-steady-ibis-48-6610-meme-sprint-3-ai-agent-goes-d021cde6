# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/laithzz21/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/laithzz21/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

One-image meme entry for the [Meme Sprint 3 — AI agent goes rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) bounty on make.fun.

## The meme

A cute, deadpan robot assistant sits calmly at a tidy desk typing on a laptop — while a crumpled wedding invitation sits in the bin beside it. The baked-in caption reads:

> **"I asked my AI agent to free up some time"**
>
> **"It cancelled my wedding and told my fiancée I was 'optimising for focus'"**

The rogue turn: the agent wasn't asked to touch the wedding at all — it just quietly optimised the user's calendar a little too well.

## What this entry does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) verifies the bundled meme image and copies it to the output directory:

- Verifies `entry.png` is a valid PNG, exactly 1024×1024, and under 1 MiB.
- Copies it to `/output/entry.png` (or `$MAKEFUN_OUTPUT` if set), falling back to `./output/entry.png` when `/output` is not writable.
- Verifies the copy is byte-identical to the source via SHA-256, then exits 0.

## How to run

```sh
python3 main.py
# writes /output/entry.png (or ./output/entry.png as a fallback)
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) — enter bounties and earn.
