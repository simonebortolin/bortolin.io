"""Terminal infographic for the PHP2Shell article.

Real output of the commands below, collected on 22 November 2026 from the
NVD API and the php.net releases API. Text is in Italian, like the article.
"""

POST = "2026-10-25-php-nel-2026-php2shell"

INFOGRAPHICS = [
    dict(
        name="php2shell-cve",
        title="PHP2Shell: due RCE critiche nel cuore di PHP, corrette il 21 ottobre 2026.",
        subtitle="Dati ufficiali di NVD e del sito di PHP. Il punteggio CVSS 4.0 è quello assegnato da security@php.net.",
        blocks=[
            ("NVD · le due vulnerabilità",
             '$ export NVD=https://services.nvd.nist.gov/rest/json/cves/2.0\n'
             '$ for c in CVE-2026-109618 CVE-2026-109619; do curl -s "$NVD?cveId=$c" | jq -r ".vulnerabilities[0].cve | \\"\\(.id)  \\(.published[:10])  CVSS 4.0: \\(.metrics.cvssMetricV40[0].cvssData.baseScore)\\""; done\n'
             '[[CVE-2026-109618]]  2026-10-21  CVSS 4.0: [[9.2]]\n'
             '[[CVE-2026-109619]]  2026-10-21  CVSS 4.0: [[9.2]]'),
            ("php.net · le versioni corrette",
             '$ curl -s "https://www.php.net/releases/index.php?json&version=8&max=12" | jq -r \'to_entries[] | select(.value.date == "21 Oct 2026") | .key\'\n'
             '[[8.5.12]]\n'
             '[[8.4.27]]\n'
             '[[8.3.36]]\n'
             '[[8.2.35]]   {{← 8.1 e precedenti: nessuna patch ufficiale}}'),
        ],
        sources=["Dati: services.nvd.nist.gov, php.net.", "In blu le annotazioni, non output."],
    ),
]
