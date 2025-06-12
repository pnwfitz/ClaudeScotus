# ClaudeScotus Supreme Court Data Repository

## Navigation Guide for Amateurs

### 🗂️ **Browse by Year**
- **[2022-2023](terms/2022-2023/)** - Justice Jackson's first term
- **[2023-2024](terms/2023-2024/)** - Recent completed term  
- **[2024-2025](terms/2024-2025/)** - Current term (ongoing)

### 👨‍⚖️ **Justice Profiles**
Individual Justice analysis and voting patterns:
- [Chief Justice Roberts](justices/roberts.md)
- [Justice Thomas](justices/thomas.md)
- [Justice Alito](justices/alito.md)
- [Justice Sotomayor](justices/sotomayor.md)
- [Justice Kagan](justices/kagan.md)
- [Justice Gorsuch](justices/gorsuch.md)
- [Justice Kavanaugh](justices/kavanaugh.md)
- [Justice Barrett](justices/barrett.md)
- [Justice Jackson](justices/jackson.md) *(joined 2022)*

### 📊 **Analysis Tools**
- [Predictions](analysis/predictions/) - ClaudeScotus prediction tracking
- [Accuracy Tracking](analysis/accuracy_tracking/) - Historical performance metrics

## Case File Structure

Each case folder contains:
```
[docket-number]_[case-name]/
├── README.md           # Case summary and outcome
├── briefs/
│   ├── petitioner_brief.pdf
│   └── respondent_brief.pdf
├── oral_arguments/
│   └── transcript.pdf
├── opinions/
│   ├── majority_opinion.pdf
│   ├── dissents/
│   └── concurrences/
└── metadata.json       # Structured case data
```

## Quick Access

**Need pure odds on a case?** → Check case README.md for our prediction confidence  
**Want to understand a Justice?** → Read their profile in `/justices/`  
**Looking for specific term?** → Navigate to `/terms/[year]/cases/`

---
*Built for legal professionals and curious amateurs alike*