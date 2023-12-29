class Extends:
    @staticmethod
    def get_or_none(klass:object, filter:dict):
        try:    
            return klass.objects.get(**filter)
        except Exception as e:
            return None