class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receive_mails = set()
        for email in emails:
            email = email.split("@")
            local_name = email[0].split("+")
            local_name = local_name[0].replace(".","")
            receive_mails.add(local_name +"@" + email[1])
        return len(receive_mails)