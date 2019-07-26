class Series {
    constructor(data) {
        this.data = data
    }

    get data() {
        for(let item in this._data) {
            console.log(item)
        }

        return this._data
    }

    set data(data) {
        this._data = data
    }
}