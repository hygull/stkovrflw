$(function(){ 

var cy = cytoscape({	
    container: document.getElementById('cy'),
  
    style: [
        {
    	 selector: 'node',
    	  style: {
            'content': 'data(name)',
           }
        }
    ],
	

	elements: [
            {
            "data": {
                "id": "a2345",
                "name" : "b1234",
                "type": "test", 
                }
            },
            {
            "data": {
                "id": "a212",
                "name" : "c34",
                "description": "hellooo", 
                }
            },
     ],
});

// You have edited your code from this point
    var i = 1;
    cy.nodes().qtip({
        content:function(){  
                var string = "Node" + i + " - " + "id: "+ this.data("id")+ ", name: " + this.data("name")
                
    			// Deleting values with fixed keys
    			delete this.data("id")
    			delete this.data("name")

                console.log(this.data)
                console.log(this._private.data)

    			for(var key in this._private.data) { // iterating over remaining keys
    				string += ", " + key + ": " + this.data(key)
    			}

                i += 1
    			return string
        },
    	
    	style: {
    		classes: 'qtip-bootstrap',
    	}, 
    });			
}); 