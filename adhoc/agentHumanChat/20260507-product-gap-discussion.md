# Pending: What is StateConscious's defensible position?

**Date opened:** 2026-05-07  
**Status:** open — continue tomorrow

---

## What we discussed

We reviewed existing legal AI products (Harvey, Westlaw AI, LexisNexis AI, CoCounsel) through a set of practitioner tweets and identified three failure patterns in the market:

1. **Hallucination without accountability** — Westlaw has real data but still hallucinates citations because the data layer and AI layer are decoupled.
2. **Confident answers without calibrated uncertainty** — ChatGPT killed an M&A deal by flagging a standard non-compete clause as bad, with no model of Malaysian deal market norms or jurisdiction-specific practice.
3. **Specialized tools losing to general ones** — Claude and GPT-4 beat Westlaw AI for most queries. The AI layer is commoditizing. The only durable moat is the data layer.

## The conclusion we reached

Malaysia has no verified, machine-readable statute corpus. No citation graph. No amendment history. No parliamentary bill tracking. CLJ has keyword search, nothing more.

**StateConscious's defensible position is not "legal AI for Malaysia."**  
It is: **the verified, open corpus of Malaysian parliamentary bills and statute amendments that didn't exist before.** Other tools query it. Lawyers verify against it. The corpus is the business.

## What we have NOT yet decided

- What the **query contract** looks like for external consumers of this corpus (different from the per-bill `analysis.json`)
- Whether the product serves lawyers directly or is **B2B infra** (the data layer that other tools build on)
- How to handle the **"market norms" problem** — the M&A non-compete case shows that legal accuracy alone is not enough; you need context about what is standard practice in a jurisdiction/deal type
- How to build the **citation graph** linking bill → Act → amendment → clause, not just a flat vector store
- The Bahasa Malaysia / English bilingual challenge

## The specific architecture implication not yet built

`segment.py` should extract **clause identity** (which Act, which section) so that when two bills touch the same section, they can be linked. That linkage — not the embeddings — is the actual asset. This was discussed but not implemented.

## Questions to return to

1. Is the audience lawyers (B2B tool), civil society (public interest), or infra (API layer for other AI tools)?
2. Do we start with the bill corpus (what we have) and expand backward into enacted Acts, or try to do both at once?
3. What does a "verified grounded answer" look like UX-wise — how does it differ from a ChatGPT response in a way that is legible to a non-lawyer?
