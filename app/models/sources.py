class Sources:

      all_sources = []

      def __init__(self,id,name,description,url,country):
            self.id = id
            self.name = name
            self.description = description
            self.url = url
            self.country = country

      @classmethod
      def get_sources(cls,id):

            response = []

            for sources in cls.all_sources:
                  if sources.id == id:
                        response.append(sources)
                        
            return response
      
 