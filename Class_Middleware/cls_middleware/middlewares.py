class my_middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One Time Initialization!!")
    
    def __call__(self,request):
        print("This is Before Views!!")
        ##############################
        ###########################
        #######################
        ####################
        response=self.get_response(request)
        print("This Is After Views!!")
        #################################
        ############################
        #######################
        ##################
        
        return response


