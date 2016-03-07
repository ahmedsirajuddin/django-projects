angular.module("BaseApp", [])
    .config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }])

    .config(['$locationProvider', function($locationProvider){
        $locationProvider.html5Mode(true);
    }])

    .factory("BaseService", ["$http", "$window", function($http, $window) {

        var cerrorMessages;

        /* This function sets self.cerrorMessages. After calling this function,
         * you should do a callback to a function on the front-end which
         * sets cerrorMessage. */
        self.accessErrors = function(data) {
             self.cerrorMessages = [];
             for (prop in data) {
                 if (data.hasOwnProperty(prop)){
                     /* if (data[prop] != null && data[prop].constructor ==  Object) {
                         self.accessErrors(data[prop]);
                     }
                     else { */
                     self.cerrorMessages.push(data[prop]);
                     // }
                 }
             }
         };

        /* All functions which call add should have a callback function
         * on the front-end which sets cerrorMessages to equal
         * BaseService.cerrorMessages. */
        self.add = {
            post: function(post, callback) {
                $http.post("/posts/", post)
                .then(function(response) {
                    $window.location.href = "/";
                }, function(response) {
                    self.accessErrors(response.data);
                    callback();
                });
            }
        };

    }
