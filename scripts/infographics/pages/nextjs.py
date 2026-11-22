"""Terminal infographic for the Next.js article.

Real output of the commands below, collected on 22 November 2026 from the
NVD API and the npm registry; the list of patched versions matches the
Next.js advisory (nextjs.org/blog/CVE-2025-66478). Text is in Italian.
"""

POST = "2025-12-07-nextjs-vulnerabilita-startup-devops-dockerfile"

INFOGRAPHICS = [
    dict(
        name="nextjs-react2shell-cve",
        title="Next.js e React Server Components: esecuzione di codice senza autenticazione, CVSS 10.",
        subtitle="Una sola vulnerabilità: la CVE assegnata a Next.js è stata respinta come doppione. Dati ufficiali di NVD, npm e Next.js.",
        blocks=[
            ("NVD · stato delle due CVE",
             '$ export NVD=https://services.nvd.nist.gov/rest/json/cves/2.0\n'
             '$ for c in CVE-2025-55182 CVE-2025-66478; do curl -s "$NVD?cveId=$c" | jq -r ".vulnerabilities[0].cve | \\"\\(.id)  \\(.vulnStatus)\\""; done\n'
             'CVE-2025-55182  Analyzed\n'
             'CVE-2025-66478  [[Rejected]]\n'
             '$ curl -s "$NVD?cveId=CVE-2025-66478" | jq -r ".vulnerabilities[0].cve.descriptions[0].value"\n'
             'Rejected reason: [[This CVE is a duplicate of CVE-2025-55182.]]'),
            ("NVD · gravità e natura",
             '$ curl -s "$NVD?cveId=CVE-2025-55182" | jq -r ".vulnerabilities[0].cve.metrics.cvssMetricV31[0].cvssData.baseScore"\n'
             '[[10.0]]\n'
             '$ curl -s "$NVD?cveId=CVE-2025-55182" | jq -r ".vulnerabilities[0].cve.descriptions[0].value" | cut -c1-74\n'
             'A [[pre-authentication remote code execution]] vulnerability exists in React S'),
            ("npm · versioni di Next.js pubblicate il 3 dicembre 2025",
             '$ npm view next time --json | jq -r \'to_entries[] | select(.value | startswith("2025-12-03")) | .key\' | grep -v -- -\n'
             '16.0.7\n'
             '15.5.7\n'
             '15.4.8\n'
             '15.1.9\n'
             '15.0.5\n'
             '15.3.6\n'
             '15.2.6   {{← le sette versioni correttive dell\'avviso Next.js}}'),
        ],
        sources=["Dati: services.nvd.nist.gov, registry npm,",
                 "nextjs.org/blog/CVE-2025-66478.",
                 "In blu le annotazioni, non output."],
    ),
]
