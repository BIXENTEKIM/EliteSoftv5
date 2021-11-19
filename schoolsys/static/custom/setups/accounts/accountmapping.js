
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    acmModal();
    getAccountmapping();
    saveAccountmapping();
    editAccountmapping();
    deleteAccountmapping();
    searchAccountMaster();
    accountMasterChange();
    searchAccountMaster2();
    accountMasterChange2();
})
function acmModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#acmModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
      $('#am-frm').empty();
      $('#am-code').val('');
       $('#amc-frm').empty();
      $('#amc-code').val('');
      $('#acm-form')[0].reset();
      $('#acm_code').val('');
}
function deleteAccountmapping() {
    $('#acmTable').on('click','.btn-deleteAccountmapping',function (s) {
        var data = $(this).closest('tr').find('#delete-accountmapping').val();
        bootbox.confirm("Are you sure want to delete this Account Mapping?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteAccountmapping/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getAccountmapping()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getAccountmapping() {
     $.ajax({
        type: 'GET',
        url: 'getAccountmapping',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#acmTable').DataTable().destroy();
       $("#acmTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#acmTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.acm_type + "</td>"
                    + "<td>" + item.acm_AccountMaster + "</td>"
                    + "<td>" + item.acm_contra_AccountMaster + "</td>"
                    + "<td>" + item.acm_desc + "</td>"
                    + "<td>" + '<form id="editAccountmapping" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-accountmapping" name="id" value=' + item.acm_code + '></form><button class="btn btn-outline-primary btn-sm btn-editAccountmapping" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteAccountmapping" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-accountmapping" name="id" value=' + item.acm_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteAccountmapping" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#acmTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveAccountmapping(){
    $('#saveAccountMapping').click(function () {
        var data=$('#acm-form').serialize();
        var url = '';
        if($('#acm_code').val()===''){
          url = 'createAccountmapping'
        }else{
            url = 'updateAccountmapping/'+$('#acm_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getAccountmapping()
            clearData()
            $('#acmModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editAccountmapping(){
    $('#acmTable').on('click','.btn-editAccountmapping',function (s) {
        var data=$(this).closest('tr').find('#edit-accountmapping').val();
        $.ajax({
            type: 'GET',
            url: 'editAccountmapping/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#acm_code').val(s.acm_code);
            $('#acm_desc').val(s.acm_desc);
            $('#acm_type').val(s.acm_type);

            if (s.accountMasterCode) {
                $('#am-code').val(s.accountMasterCode)

                var $newOption = $("<option selected='selected' value='" + s.accountMasterCode + "'>'+s.accountMasterName+'</option>").val(s.accountMasterCode.toString()).text(s.accountMasterName)

                $('#am-frm').append($newOption).trigger('change');
            } else {
                $('#am-code').val('')

                $('#am-frm').empty();

            }

             if (s.accountMasterCode2) {
                $('#amc-code').val(s.accountMasterCode2)

                var $newOption = $("<option selected='selected' value='" + s.accountMasterCode2 + "'>'+s.accountMasterName2+'</option>").val(s.accountMasterCode2.toString()).text(s.accountMasterName2)

                $('#amc-frm').append($newOption).trigger('change');
            } else {
                $('#amc-code').val('')

                $('#amc-frm').empty();

            }


        $('#acmModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
function searchAccountMaster() {
     $('#am-frm').select2({
           placeholder: 'AccountMaster',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchAccountMaster',
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

function accountMasterChange(){
    $('#am-frm').on('select2:select', function (e) {
    var data = e.params.data;
    $('#am-code').val(data.id)
    $('#am-desc').val(data.text)

});
    $("#am-frm").on("select2:unselecting", function(e) {
    $('#am-code').val('')
    $('#am-desc').val('')
 });
}
 ///////////

 function searchAccountMaster2() {
     $('#amc-frm').select2({
           placeholder: 'AccountMaster2',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchAccountMaster2',
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

function accountMasterChange2(){
    $('#amc-frm').on('select2:select', function (e) {
    var data = e.params.data;
    $('#amc-code').val(data.id)
    $('#amc-desc').val(data.text)

});
    $("#amc-frm").on("select2:unselecting", function(e) {
    $('#amc-code').val('')
    $('#amc-desc').val('')
 });
}

