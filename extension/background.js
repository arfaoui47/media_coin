// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Called when the user clicks on the browser action.
chrome.tabs.onActivated.addListener(function(info) {chrome.tabs.getSelected(null, (tab) => {getOUt(tab)

})});
chrome.tabs.onUpdated.addListener(function(info) {chrome.tabs.getSelected(null, (tab) => {getOUt(tab)

})});
const getOUt = (tab) => {
  if(/facebook.com*/.test(tab.url)){

    var distance = 60;

	var x = setInterval(function() {
	  distance--;
	  if (distance < 0) {
	    clearInterval(x);
		chrome.tabs.update(tab.id, {url: "http://stackoverflow.com"});
	  }
	}, 1000);
  }
}
