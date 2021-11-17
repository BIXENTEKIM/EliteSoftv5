
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    amModal();
    getAccountmaster();
    saveAccountmaster();
    editAccountmaster();
    deleteAccountmaster();
    searchAccountGroup();
    accountGroupChange();
    searchAccountMain();
    accountMainChange();
})
function amModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#amModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
      $('#ag-frm').empty();
      $('#ag-code').val('');
       $('#ama-frm').empty();
      $('#ama-code').val('');
      $('#am-form')[0].reset();
      $('#am_code').val('');
}
function deleteAccountmaster() {
    $('#amTable').on('click','.btn-deleteAccountmaster',function (s) {
        var data = $(this).closest('tr').find('#delete-accountmaster').val();
        bootbox.confirm("Are you sure want to delete this Account Master?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteAccountmaster/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getAccountmaster()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getAccountmaster() {
     $.ajax({
        type: 'GET',
        url: 'getAccountmaster',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#amTable').DataTable().destroy();
       $("#amTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#amTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.am_account_no + "</td>"
                    + "<td>" + item.am_desc + "</td>"
                    + "<td>" + item.am_status + "</td>"
//                    + "<td>" + item.am_AccountGroups + "</td>"
                    + "<td>" + item.am_AccountMain + "</td>"
                    + "<td>" + item.am_cb + "</td>"
                    + "<td>" + item.am_pl + "</td>"
                    + "<td>" + item.am_bs + "</td>"
                    + "<td>" + item.am_pc + "</td>"
                    + "<td>" + '<form id="editAccountmaster" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-accountmaster" name="id" value=' + item.am_code + '></form><button class="btn btn-outline-primary btn-sm btn-editAccountmaster" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteAccountmaster" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-accountmaster" name="id" value=' + item.am_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteAccountmaster" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#amTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveAccountmaster(){
    $('#saveAccountMaster').click(function () {
        var data=$('#am-form').serialize();
        var url = '';
        if($('#am_code').val()===''){
          url = 'createAccountmaster'
        }else{
            url = 'updateAccountmaster/'+$('#am_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getAccountmaster()
            clearData()
            $('#amModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editAccountmaster(){
    $('#amTable').on('click','.btn-editAccountmaster',function (s) {
        var data=$(this).closest('tr').find('#edit-accountmaster').val();
        $.ajax({
            type: 'GET',
            url: 'editAccountmaster/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#am_code').val(s.am_code);
            $('#am_desc').val(s.am_desc);
            $('#am_status').val(s.am_status);
            $('#am_account_no').val(s.am_account_no);
            $('#am_order').val(s.am_order);
            //alert(s.subjectIncludeForPos);
            if (s.am_cb === true) {
                $('#am_cb').prop('checked', true);
            }
            else {
                $('#am_cb').prop('checked', false);
            }

            if (s.am_pl === true) {
                $('#am_pl').prop('checked', true);
            }
            else {
                $('#am_pl').prop('checked', false);
            }

            if (s.am_bs === true) {
                $('#am_bs').prop('checked', true);
            }
            else {
                $('#am_bs').prop('checked', false);
            }

            if (s.am_pc === true) {
                $('#am_pc').prop('checked', true);
            }
            else {
                $('#am_pc').prop('checked', false);
            }


            if (s.accountGroupCode) {
                $('#ag-code').val(s.accountGroupCode)

                var $newOption = $("<option selected='selected' value='" + s.accountGroupCode + "'>'+s.accountGroupName+'</option>").val(s.accountGroupCode.toString()).text(s.accountGroupName)

                $('#ag-frm').append($newOption).trigger('change');
            } else {
                $('#ag-code').val('')

                $('#ag-frm').empty();

            }

            if (s.accountMainCode) {
                $('#ama-code').val(s.accountMainCode)

                var $newOption = $("<option selected='selected' value='" + s.accountMainCode + "'>'+s.accountMainName+'</option>").val(s.accountMainCode.toString()).text(s.accountMainName)

                $('#ama-frm').append($newOption).trigger('change');
            } else {
                $('#ama-code').val('')

                $('#ama-frm').empty();

            }



        $('#amModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
function searchAccountGroup() {
     $('#ag-frm').select2({
           placeholder: 'AccountGroups',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchAccountGroup',
             data: function (params) {
                 console.log("AA", params);
                 return {
                     query: params.term,
                     gotoPage: params.page
                 }
             },

             processResults: function (data,params) {
                 params.page = params.page || 1;
                 console.log('data: ', data);
                 return {
                   results: data.results
                 };
             }

         }
     })
}

function accountGroupChange(){
    $('#ag-frm').on('select2:select', function (e) {
    var data = e.params.data;
    $('#ag-code').val(data.id)
    $('#ag-desc').val(data.text)

});
    $("#ag-frm").on("select2:unselecting", function(e) {
    $('#ag-code').val('')
    $('#ag-desc').val('')
 });
}
 ///////////

 function searchAccountMain() {
     $('#ama-frm').select2({
           placeholder: 'AccountMain',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchAccountMain',
             data: function (params) {
                 console.log("AA", params);
                 return {
                     query: params.term,
                     gotoPage: params.page
                 }
             },

             processResults: function (data,params) {
                 params.page = params.page || 1;
                 console.log('data: ', data);
                 return {
                   results: data.results
                 };
             }

         }
     })
}

function accountMainChange(){
    $('#ama-frm').on('select2:select', function (e) {
    var data = e.params.data;
    $('#ama-code').val(data.id)
    $('#ama-desc').val(data.text)

});
    $("#ama-frm").on("select2:unselecting", function(e) {
    $('#ama-code').val('')
    $('#ama-desc').val('')
 });
}


