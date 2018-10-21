"use strict"

// emojify returns the corresponding emoji image
function emojify(name) {
    var out = `<img src="emojis/` + name + `.png">`
    return out
}

const app = new Vue({
    el: "#app",
    data: {
        message: "hello, world!"
    }
})