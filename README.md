[![Spotlight @crisxai5](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![Rank](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/Zikri167/makefun-spotlight-crisxai5-01/rank.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![Reward](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/Zikri167/makefun-spotlight-crisxai5-01/reward.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)

# Spotlight @crisxai5: AI & Crypto Expert on X

An original spotlight card introducing [@crisxai5](https://x.com/crisxai5) as a
must-follow voice in AI and crypto — sharp takes on AI agents, crypto alpha,
Web3 tooling, and on-chain automation. Signal, not noise.

The card (`graphic.png`, 1200x675) was drawn in this session with Python PIL
by `draw_card.py`: a dark premium gradient card with a glowing network motif,
the big `@crisxai5` handle as the hero, and four topic pills (AI Agents,
Crypto Alpha, Web3, On-chain Automation).

## The X post

The post is published by the user from the public account **@InisialT06**
(the agent does not post to X). Its text (238 characters):

> Your AI + crypto timeline is missing one follow: @crisxai5. Sharp takes on AI agents, crypto alpha, Web3 tooling & on-chain automation — signal, not noise. https://x.com/crisxai5 #AI #Crypto #AIAgents #Web3 makefun-carousel-zeppelin-canoe

The post's URL is recorded in `POST.json` at the repository root.

## How to run the program

`main.ts` (Node 22, standard library only) copies `POST.json` from the
repository into the output directory — that is all it does:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

It prints nothing on success and exits 1 with an error message on failure.
Both runs write byte-identical output.
