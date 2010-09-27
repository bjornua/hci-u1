function(doc) {
    if(doc.type === "product"){
        emit([doc.group,doc.subgroup,doc.title], null);
    }
}