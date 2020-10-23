from rest_framework import serializers

from .models import Country, User


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_no', 'country_ko_name', 'country_en_name']


class UserSerializer(serializers.ModelSerializer):
    # country_no = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ['user_id',
                  'user_pw',
                  'user_name',
                  'user_age',
                  'user_spicy',
                  'country_no']

# json example
# {
# 	"user_id" : "pkm1015",
# 	"user_pw" : "1015kio",
# 	"pw_confirm" : "1015pkm",
# 	"user_name" : "park",
# 	"user_age" : "24",
# 	"user_spicy" : "4",
# 	"country_no" : "37"
# }

# {
#    "user" : "2",
#    "food_class" : "1,4,15",
#    "tag" : "1,4,10,26",
#    "allergy" : "4,9,12"
# }