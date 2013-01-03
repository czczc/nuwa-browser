'use strict';


// Declare app level module which depends on filters, and services
angular.module('nuwaBrowser', ['nuwaBrowser.filters', 'nuwaBrowser.services', 'nuwaBrowser.directives']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.
      when('/modules', {
        templateUrl: 'partials/modules.html',
        controller: ModuleListCtrl
      }).
      when('/packages', {
        templateUrl: 'partials/packages.html',
        controller: PackageListCtrl
      }).
      when('/configurables', {
        templateUrl: 'partials/configurables.html',
        controller: ConfigurableListCtrl
      }).
      when('/configurables/:configurableName', {
        templateUrl: 'partials/configurable.html',
        controller: ConfigurableDetailCtrl
      });
    $routeProvider.otherwise({redirectTo: '/modules'});
  }]);
  