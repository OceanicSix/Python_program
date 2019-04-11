#include <eosiolib/eosio.hpp>

using namespace eosio;
using namespace std;

class [[eosio::contract("student")]] student  : public eosio::contract {

public:
  using contract::contract;

  student(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}

  [[eosio::action]]
  void upsert(name user, string first_name,string last_name,string grade) {
    require_auth( user );
    student_table table(_code,_code.value);
  auto iterator = table.find(user.value);
  if( iterator == table.end() ){
  table.emplace(user,[&] (auto& row){
    row.key=user;
    row.first_name=first_name;
    row.last_name=last_name;
    row.grade=grade;
  });
}else {
      table.modify(iterator, user, [&]( auto& row ) {
        row.key = user;
        row.first_name = first_name;
        row.last_name = last_name;
	row.grade=grade;
      });
    }
}


private:
  struct [[eosio::table]] student_info {
      name key;
      string first_name;
      string last_name;
      string grade;
      uint64_t primary_key() const { return key.value; }
    };
    typedef eosio::multi_index<"table"_n, student_info> student_table;

};

EOSIO_DISPATCH( student, (upsert))
