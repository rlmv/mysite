

var viewsize = view.size;

var atoms = new Group();
var edges = new Group();
var numAtoms = 7;

var rand;
var rad;

// check that an Item atom is in view, and correct it if not.
function inView(atom) {
    var bounds = atom.bounds;
    
    var farLeft = bounds.x;
    var farRight = bounds.x + bounds.width;
    var farTop = bounds.y;
    var farBottom = bounds.y + bounds.height;
    
    if (farLeft < 0) {
        atom.position.x -= farLeft;
    }
    else if (farRight > view.size.width) {
        atom.position.x -= farRight - view.size.width;
    }
    if (farTop < 0) {
        atom.position.y -= farTop;
    }
    else if (farBottom > view.size.height) {
        atom.position.y -= farBottom - view.size.height;
    }
}


function init() {

    for (i = 0; i < numAtoms; i++) {
        rand = new Point.random();
        rand.x *= viewsize.width;
        rand.y *= viewsize.height;
        rad = 5 + Math.random() * 10; // radius
        
        circle = new Path.Circle(rand, rad);
        circle.fillColor = 'red';
        
        atoms.addChild(circle);
        inView(circle); 
    }
    
    
    for (var i=0; i < numAtoms; i++) {
        for (var j=i; j < numAtoms; j++) {
            if (atoms.children[i] !== atoms.children[j]) {
                var link = new Path(atoms.children[i].position, atoms.children[j].position);
                console.log(link);
                link.strokeColor = 'black';
                
                edges.addChild(link);
            }
        }
    }
    atoms.moveAbove(edges);
    
}


init();

function onFrame(event) {
}
    

function onMouseUp(event) {
    for (var i=0; i < atoms.length; i++) {
        atoms[i].fillColor = 'red';
    }
    
    // there might be an error in the source code here...
    // it doesn't work for params (0,1);
    edges.removeChildren(edges.children.length-1);
}
