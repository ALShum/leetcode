class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email = set()
        for e in emails:
            at = e.index('@')
            name = e[:at].replace('.', '')
            domain = e[at+1:]

            plus = name.index('+') if '+' in name else len(name)
            name = name[:plus]
            email.add(name + '@' + domain)

        return len(email)
