pragma solidity ^0.4.0;
contract Tourist Ticket{

    address owner;
    uint256 previousBalance;

    event addedFunds(address whoAdded, uint256 howMuch);

    function Tickter() {
        owner = msg.sender;
        mods[owner] = mod("Tickter", true);
        members[owner] = member(true, true, 0, 0);
        previousBalance = this.balance;
    }

    struct member{
        bool isMember;
        bool isPermitted;
        //uint maxAmount;
        uint256 TicketGranted;
        int256 amountAddedToThePool;
    }

    struct mod{
        string name;
        bool status;
    }

    mapping(address => member) members;
    mapping(address => mod) mods;
    mapping(address => uint256) TicketGranted;

    modifier onlyowner(){
        require(msg.sender == owner);

        _;
    }

    modifier onlymods(){
        require(mods[msg.sender].status == true);
            _;
    }

    modifier onlymember(){
        require(members[msg.sender].isMember == true);
            _;
    }

    function addMods(address _modAddress, string _modName) onlyowner{
        mods[_modAddress] = mod(_modName, true);
    }

    function addMembers(address _memberaddress) onlymods{
        members[_memberaddress] = member(true, true, 0, 0);
    }

    function removeMembers(address _memberaddress) onlymods{
        delete members[_memberaddress];
    }


    function requestTicket(uint256 loanAmount) onlymember returns(bool status){
        if(members[msg.sender].isPermitted && int(loanAmount) <= 2*members[msg.sender].amountAddedToThePool && TicketAmount <= this.balance/2){
            members[msg.sender].isPermitted = false;
            members[msg.sender].TicketGranted = TicketAmount;
            members[msg.sender].amountAddedToThePool -= int(TicketAmount);
            msg.sender.transfer(TicketAmount);
            // previousBalance = this.balance;
            return true;
        }
        else{
            revert();
        }
    }
    
    function getTicketGranted() constant returns(uint256){
        return members[msg.sender].TicketGranted;
    }

    function getBalance() constant returns(uint256){
        return this.balance;
    }

    function getAmountAdded() constant returns(int256){
        return members[msg.sender].amountAddedToThePool;
    }
}
