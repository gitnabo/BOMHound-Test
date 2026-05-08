# BOMHound Agent Instructions

BOMHound is a local-first prototype for collecting and reviewing supplier compliance documentation from BOM spreadsheets.

The broader product vision is:
- Given a BOM spreadsheet with internal part numbers, part names, descriptions, supplier/manufacturer information, and manufacturer part numbers, assemble compliance documentation for each part.
- Long-term documentation targets may include REACH, RoHS, China RoHS, PFAS, Prop 65, and Conflict Minerals.
- Documentation may eventually be collected by searching supplier/manufacturer websites or by contacting suppliers when documents cannot be found directly.
- The product should provide a clear web-based summary of documentation status.
- The product should preserve supplier communication history when outreach is required.
- The product must not spam suppliers.

Current MVP scope:
- Start with REACH/RoHS only.
- Use fake/internal supplier contacts only.
- Run locally.
- Treat OneDrive as a synced local folder.
- Use human approval before every email or spreadsheet update.

Development rules:
- Make only small, scoped changes requested by the user.
- Build one milestone at a time.
- Do not add real email sending unless explicitly requested.
- Do not add inbox monitoring unless explicitly requested.
- Do not add OneDrive API integration unless explicitly requested.
- Do not add AI document review unless explicitly requested.
- Do not add database functionality unless explicitly requested.
- Do not modify or write back to the original Excel BOM unless explicitly requested.
- Do not implement supplier website search, supplier contact discovery, China RoHS, PFAS, Prop 65, or Conflict Minerals in the first milestone.
