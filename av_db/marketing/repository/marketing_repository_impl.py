from account_profile.repository.account_profile_repository_impl import AccountProfileRepositoryImpl
from marketing.entity.marketing import Marketing
from marketing.repository.marketing_repository import MarketingRepository
from company_report.repository.company_report_repository_impl import CompanyReportRepositoryImpl


class MarketingRepositoryImpl(MarketingRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountProfileRepository = AccountProfileRepositoryImpl.getInstance()
            cls.__instance.__companyReportRepository = CompanyReportRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def makeCount(self, email, product_id, purchase):
        profile = self.__accountProfileRepository.findByEmail(email)
        product = self.__companyReportRepository.findByCompanyReportId(product_id)
        marketing, created = Marketing.objects.get_or_create(
            account=profile.account,
            product=product
        )

        if not created:
            marketing.click_count += 1  # 이미 존재하면 클릭 수 증가

        marketing.purchase = purchase  # 구매 여부 업데이트
        marketing.save()  # 변경 사항 저장
        return marketing
