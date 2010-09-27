function(doc) {
    if(doc.type === "product"){
        emit([doc.subgroup, doc.title], null);
    }
}