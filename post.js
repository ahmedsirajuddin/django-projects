angular.module("PostPageApp", ["BaseApp"])
    .controller("MainCtrl", ["BaseService", function(BaseService) {
    
        var self = this;

        self.add = function() {
            BaseService.add.post(self.post, function() {
                self.cerrorMessages = BaseService.cerrorMessages;
            });
        };

        self.logoutUser = function() {
            BaseService.logout();
        };

    }]);
