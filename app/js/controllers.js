'use strict';

/* Controllers */

// Module Controller
function ModuleListCtrl($scope, $http) {
  $http.get('nuwa/modules.json').
    success(function(data) {
      $scope.modules = data;
    }).
    error(function () {
      alert("ModuleListCtrl: cannot find json file");
    });

  $scope.orderBy = 'name';

  $scope.shortUrl = function (module) {
    var url = module.location;
    if (url == "") {
      return "";
    }
    else if (module.extra == "conf") {
      return url+"/src";
    }
    else {
      url += "/python/";
      url += module.name.replace(/\./g, '/');
      if (module.extra == "") {
        url += ".py";;
      }
    }
    return url;
  };

  $scope.tracUrl = function (module) {
    var url = "http://dayabay.ihep.ac.cn/tracs/dybsvn/browser/dybgaudi/trunk/";
    return url + $scope.shortUrl(module);
  };

  $scope.svnUrl = function (item) {
    var url = "http://dayabay.ihep.ac.cn/svn/dybsvn/dybgaudi/trunk/";
    return url + $scope.shortUrl(item);
  };

  $scope.redirect = function () {
    var url = $scope.tracUrl($scope.filtered[0]);
    window.location = url;
  }
}
ModuleListCtrl.$inject = ['$scope', '$http'];


// Package Controller
function PackageListCtrl($scope, $http) {
  $http.get('nuwa/packages.json').
    success(function(data) {
      $scope.packages = data;
    }).
    error(function () {
      alert("PackageListCtrl: cannot find json file");
    });

  $scope.orderBy = 'name';

  $scope.shortUrl = function (item) {
    return item.location;
  };

  $scope.tracUrl = function (item) {
    var url = "http://dayabay.ihep.ac.cn/tracs/dybsvn/browser/";
    return url + $scope.shortUrl(item).replace(/(\w+)\//, '$1'+'/trunk/');
  };

  $scope.svnUrl = function (item) {
    var url = "http://dayabay.ihep.ac.cn/svn/dybsvn/";
    return url + $scope.shortUrl(item).replace(/(\w+)\//, '$1'+'/trunk/');
  };

  $scope.doxgenUrl = function (item) {
    var url = "http://dayabay.bnl.gov/dox/";
    return url + item.name + "/html/annotated.html";
  };

  $scope.redirect = function () {
    var url = $scope.tracUrl($scope.filtered[0]);
    window.location = url;
  }
}
PackageListCtrl.$inject = ['$scope', '$http'];

// Configurable Controller
function ConfigurableListCtrl($scope, $http) {
  $http.get('nuwa/configurables.json').
    success(function(data) {
      $scope.configurables = data;
    }).
    error(function () {
      alert("ConfigurableListCtrl: cannot find json file");
    });

  $scope.orderBy = 'name';

  $scope.redirect = function () {
    var url = '#/configurables/'+$scope.filtered[0].name;
    // alert(url);
    window.location = url;
  }
}
ConfigurableListCtrl.$inject = ['$scope', '$http'];


// Configurable Controller
function ConfigurableDetailCtrl($scope, $http, $routeParams) {
  $scope.configurableName = $routeParams.configurableName
  $http.get('nuwa/configurables/'+$scope.configurableName+'.json').
    success(function(data) {
      $scope.properties = data;
    }).
    error(function () {
      alert("ConfigurableDetailCtrl: cannot find json file");
    });

  $scope.orderBy = 'name';
}
ConfigurableDetailCtrl.$inject = ['$scope', '$http', '$routeParams'];
