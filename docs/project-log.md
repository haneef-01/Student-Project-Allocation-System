# Project Log

## 2026-10-27: Decision: how I record my project
- What: keep running notes instead of writing report chapters as I go
- Alternatives considered: writing chapters as I build
- Why: this is done to avoid forgetting what has been done in the software and updating what has been done in the report.
- so we take as much notes as possible so that when writing the report we are updated and never forget what we have done.
- the software may change as I build it, so a finished chapter could end up describing something I no longer do. Short notes are easy to update, and I turn them into the report at the end.
- Report section it feeds: Introduction / Method

## 2026-11-4: Decision: Structure of Repository
- What: Seperated backend/matching (pure python) from backend/app (web code)
- Alternatives considered: one backend folder with everything together
- Why: keeping the matching algorithm separate from the web code means I can test it on small examples I check by hand, swap in other algorithms to compare in my evaluation, and keep the web layer simple.
- Report section it feeds: Design
