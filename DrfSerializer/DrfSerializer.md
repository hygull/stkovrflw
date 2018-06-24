**@No-one**, I will suggest you to define your models as follows.

> Use **ForeignKey()** for nested dictionary like `{'day': 20, 'month': 'June', 'year': 1998}`.

	class Dob(models.Model):
		day = models.IntegerField()
		month = models.CharField(max_length=10)
		year = models.IntegerField()

		def __str__(self):
			return str(self.day)

	class User(models.Model):
		name = models.CharField(max_length=50, null=False, blank=False)
		age = models.IntegerField()
		dob = models.ForeignKey(Dob, on_delete=models.CASCADE, null=False)

		def __str__(self):
			return self.name

Finally, define your serializers like this.

	class DobSerializer(serializers.HyperlinkedModelSerializer):
	    class Meta:
	        model = Dob 
	        fields = ('day', 'month', 'year')

	class UserSerializer(serializers.HyperlinkedModelSerializer):
	    dob = DobSerializer(many=False, read_only=True);

	    class Meta:
	        model = User
	        fields = ('name', 'age', 'dob');
