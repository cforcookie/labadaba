pragma solidity <=0.8.7; 
 
contract A { 
 
    struct Transfer { 
        uint id; 
        address giver; 
        address taker; 
        uint value; 
        bytes32 code; 
        string catigory; 
        string dyscription; 
        bool commision_giver; 
        bool used_shablon; 
        bool status; 
    } 
 
    struct Shablon { 
        uint id; 
        string catigory; 
        uint[] value; 
    } 
 
    struct Require_to { 
        uint id; 
        address giver; 
        bool status; 
        bool chanle; 
    } 
 
    mapping(address => uint[]) public id_giver; 
    mapping(address => uint[]) public id_taker; 
 
    mapping(address => bool) public user_rule; 
    address[] public admins; 
 
    Transfer[] public transfers; 
    Shablon[] public shablons; 
    Require_to[] public require_to; 
 
    function create_transfer(address taker, uint value, bytes32 code, string memory catigory,  
    string memory dyscription, bool commision_giver, bool used_shablon) public payable { 
        require(msg.sender != taker, "You can't send money to yourself"); 
        require(msg.sender.balance > value, "Value less"); 
        uint id = transfers.length; 
        transfers.push(Transfer(id, msg.sender, taker, value, code, catigory, dyscription, commision_giver, used_shablon, false)); 
        id_giver[msg.sender].push(id); 
        id_taker[msg.sender].push(id); 
        msg.value; 
        if (commision_giver == false && used_shablon == true) { 
            uint commision = (value/100*20)/admins.length; 
            for (uint i = 0; i < admins.length; i++) { 
                payable(admins[i]).transfer(commision); 
            } 
        } 
    } 
 
    function clime_transfer(uint id) public payable { 
        require(transfers[id].taker == msg.sender, "Not for you"); 
        require(transfers[id].status == false, "Transfer complite"); 
        payable(msg.sender).transfer(transfers[id].value); 
        if (transfers[id].commision_giver == true && transfers[id].used_shablon == true) { 
            uint commision = (transfers[id].value/100*20)/admins.length; 
            for (uint i = 0; i < admins.length; i++) { 
                payable(admins[i]).transfer(commision); 
            } 
        } 
        transfers[id].status = true; 
    } 
 
    function chanle_transfer(uint id) public payable{ 
        require(transfers[id].giver == msg.sender, "You not gived it"); 
        require(transfers[id].status == false, "Transfer complite"); 
        transfers[id].status = true; 
        payable(msg.sender).transfer(transfers[id].value); 
    }  
 
    function create_require() public { 
        require(user_rule[msg.sender] == false, "You allready admin"); 
        require_to.push(Require_to(require_to.length, msg.sender, false, false)); 
    } 
 
    function confirm_require(uint id) public { 
        require(user_rule[msg.sender] == true, "Only for admins"); 
        require(require_to[id].status == false && require_to[id].chanle == false, "Require allready complite"); 
        user_rule[require_to[id].giver] = true; 
        admins.push(require_to[id].giver); 
        require_to[id].status = true; 
    } 
 
    function chanle_require(uint id) public { 
        require(user_rule[msg.sender] == true, "Only for admins"); 
        require(require_to[id].status == false && require_to[id].chanle == false, "Require allready complite"); 
        require_to[id].chanle = true; 
    } 
 
 
}