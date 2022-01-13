from django.contrib.auth.models import AnonymousUser

class A:
    pass

def clear_cart_anonymous_user(request):
    if request.session.get("cart"):
        request.session["cart"] = []  


def add_to_cart_anonymous_user(request, product_id, quantity):
    if not isinstance(request.user, AnonymousUser):
        pass
    else:
        if not request.session.get("cart"):
            request.session["cart"] = [{"product": product_id, "quantity": quantity}]
        else:
            flag = True
            for item in request.session["cart"]:
                if item.get("product") == product_id:
                    print(item["quantity"])
                    flag = False
                    item["quantity"] = int(item["quantity"]) + int(quantity)
                    print(request.session["cart"]) 
                    request.session.save()
                    break
            if flag:
                request.session["cart"].append({"product": product_id, "quantity": quantity})
                request.session.save()

def show_cart_anonymous_user(request):
    pass