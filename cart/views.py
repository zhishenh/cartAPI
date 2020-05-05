from .models import CartItem
from .serializer import CartItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .common.constant_enum import Message, StatusCode
from .common.common_response import CommonResponse


# Create your views here.
def _validate_delete_params(data):
    print(data)
    if "user_id" not in data or "item_number" not in data:
        return False


def _validate_id(user):
    print("Validating User ID = {}".format(user))


class CartItemAPIView(APIView):

    """
    Handle HTTP GET method
    Get all items in the cart
    """
    def get(self, request):
        user_id = self.request.query_params.get("user_id")
        _validate_id(user_id)
        cart_items = CartItem.objects.filter(user_id=user_id)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(CommonResponse(StatusCode.SUCCESS.value, Message.GET_SUCCESS.value, serializer.data).__dict__)

    """
    Handle HTTP GET method
    Get all items in the cart
    """
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        # Validate the parameters
        if serializer.is_valid():
            user_id = request.data["user_id"]
            _validate_id(user_id)
            item_number = request.data["item_number"]
            qty = request.data["qty"]

            # Update the quantity of a given item
            try:
                cart_item = CartItem.objects.get(user_id=user_id, item_number=item_number)
                cart_item.qty += qty
                if cart_item.qty > 0:
                    cart_item.save()
                else:
                    cart_item.delete()
                return Response(CommonResponse(code=StatusCode.SUCCESS.value,
                                               message=Message.UPDATE_SUCCESS.value,
                                               data=[]).__dict__)
            except CartItem.DoesNotExist:
                if qty < 0:
                    return Response(CommonResponse(code=StatusCode.FAIL.value,
                                                   message=Message.UPDATE_ERROR.value,
                                                   data=[]).__dict__)
                serializer.save()
                return Response(CommonResponse(code=StatusCode.SUCCESS.value,
                                               message=Message.UPDATE_SUCCESS.value,
                                               data=[]).__dict__)
        else:
            return Response(CommonResponse(code=StatusCode.FAIL.value,
                                           message=Message.PARAMS_ERROR.value,
                                           data=[]).__dict__)

    """
    Handle HTTP DELETE Method
    Delete item in the cart
    """
    def delete(self, request):

        # Validate the parameters
        valid = _validate_delete_params(request.data)
        if not valid:
            return Response(CommonResponse(code=StatusCode.FAIL.value,
                                           message=Message.PARAMS_ERROR.value,
                                           data=[]).__dict__)
        user_id = request.data["user_id"]
        item_number = request.data["item_number"]
        _validate_id(user_id)

        # Delete cart item
        try:
            cart_item = CartItem.objects.get(user_id=user_id, item_number=item_number)
            cart_item.delete()
            return Response(CommonResponse(code=StatusCode.SUCCESS.value,
                                           message=Message.DELETE_SUCCESS.value,
                                           data=[]).__dict__)
        except CartItem.DoesNotExist:
            return Response(CommonResponse(code=StatusCode.FAIL.value,
                                           message=Message.DELETE_ERROR.value,
                                           data=[]).__dict__)
