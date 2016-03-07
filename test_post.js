describe('Controller: MainCtrl', function() {
    var ctrl, mockBaseService;

    beforeEach(function() {

        mockBaseService = {
            cerrorMessages: 'whatever',
            add: { post: function(something, cb) { cb() } },
        };

        module('BaseApp', function($provide) {
            $provide.value('BaseService', mockBaseService);
        });

        module('PostPageApp');

        inject(function($controller) {
            ctrl = $controller('MainCtrl', {
            });
        });
    });

    it('add() calls through to BaseService.add.post. ' +
        'BaseService.add.post is called with ctrl.post and a callback function ' +
        'which sets cerrorMessages', function() {
        spyOn(mockBaseService.add, 'post').and.callThrough();
        ctrl.post = "{'post': 'test post'}"
        ctrl.add();

        expect(mockBaseService.add.post).toHaveBeenCalledWith(ctrl.post, jasmine.any(Function));
        expect(ctrl.cerrorMessages).toBe(mockBaseService.cerrorMessages);
    });
});
