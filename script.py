from models import CreditApplication

contract_id = 32812
credit_app = CreditApplication.objects.select_related('contract').prefetch_related('products').get(contract=contract_id)
producers = credit_app.products.values_list('producer', flat=True).distinct()
