# Project Hunt source list

This public repo holds one file the Project Hunt app reads: [`sources.json`](sources.json), the list of job boards and feeds it checks for Bengali AI data, transcription and language projects.

The app downloads it from
`https://raw.githubusercontent.com/TheAshikSarker/project-hunt-config/main/sources.json`,
keeps the last good copy on the phone, and falls back to a copy bundled inside the app. Nothing personal is ever stored here; the app's code and your data live elsewhere.

## Editing

Edit `sources.json` on GitHub (pencil icon) and commit. Phones pick up the change on their next refresh.

- **Switch a broken source off:** set `"enabled": false`. It turns off on every phone. (A source you switch off yourself on the Sources screen stays off whatever this file says.)
- **Add a company that uses Lever, Greenhouse, Recruitee or Ashby:** copy an entry and change `id`, `name`, `type` and `slug`. The slug is the company part of its jobs URL, for example `rws` in `jobs.lever.co/rws`.
- **Add a feed:** use `"type": "RSS"` with a full `https://` URL.

Every change is checked by the **Validate sources.json** action. A red X means the app would reject or misread the file, so fix it before relying on it. The app also ignores a file it cannot parse and keeps using the last good one.

## Fields

| Field | Meaning |
|---|---|
| `id` | Unique, never change it once used (the app keys listings and your on/off choice by it) |
| `name` | Shown in the app |
| `type` | `ATS_LEVER`, `ATS_GREENHOUSE`, `ATS_RECRUITEE`, `ATS_ASHBY`, `BOARD_REMOTIVE` or `RSS` |
| `slug` | Company name on the job board (ATS types) |
| `url` | Feed address (RSS) |
| `keywords` | Search words (Remotive) |
| `enabled` | `false` switches the source off on every phone |
| `fetchIntervalHours` | How often to check, 1 to 168 |
| `tosChecked` | `true` once the board's terms were checked for this use |
| `notes` | What was checked and any limits (rate, attribution) |
