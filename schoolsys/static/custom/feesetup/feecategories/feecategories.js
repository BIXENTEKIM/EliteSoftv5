
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    feesetupModal();
    getFeesetup();
    saveFeesetup();
    editFeesetup();
    deleteFeesetup();
    searchFeesetup();
})
function feesetupModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#feeModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
//      $('#dorm-form').empty();
      $('#feesetup-form')[0].reset();
      $('#category_code').val('');
}
function deleteFeesetup() {
    $('#feeTable').on('click','.btn-deleteFeesetup',function (s) {
        var data = $(this).closest('tr').find('#delete-feesetup').val();
            bootbox.confirm("Are you sure want to delete this Fee Setups?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteFeesetup/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getFeesetup()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getFeesetup() {
     $.ajax({
        type: 'GET',
        url: 'getFeesetup',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#feeTable').DataTable().destroy();
       $("#feeTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#feeTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.category_name + "</td>"
                    + "<td>" + item.category_desc + "</td>"
                    + "<td>" + item.default + "</td>"
                    + "<td>" + '<form id="editFeesetup" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-feesetup" name="id" value=' + item.category_code + '></form><button class="btn btn-outline-primary btn-sm btn-editFeesetup" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteFeesetup" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-feesetup" name="id" value=' + item.category_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteFeesetup" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#feeTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveFeesetup(){
    $('#saveFeeCat').click(function () {
        var data=$('#feesetup-form').serialize();
        var url = '';
        if($('#category_code').val()===''){
          url = 'createFeesetup'
        }else{
            url = 'updateFeesetup/'+$('#category_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getFeesetup()
            clearData()
            $('#feeModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editFeesetup(){
    $('#feeTable').on('click','.btn-editFeesetup',function (s) {
        var data=$(this).closest('tr').find('#edit-feesetup').val();
        $.ajax({
            type: 'GET',
            url: 'editFeesetup/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            //alert(val(s.dorm-code));
            // alert((s.dormCode));
            $('#category_code').val(s.category_code);
            $('#category_name').val(s.category_name);
            $('#category_desc').val(s.category_desc);
            $('#default').val(s.default);



        $('#feesetupModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
//
//function searchFeesetup() {
//     $('#dorm-frm').select2({
//           placeholder: 'Dorms',
//           allowClear: true,
//           width: '100%' ,
//           ajax: {
//             delay: 250,
//             url: 'searchDorm',
//             data: function (params) {
//                 console.log("AA", params);
//                 return {
//                     query: params.term,
//                     gotoPage: params.page
//                 }
//             },
//
//             processResults: function (data,params) {
//                 params.page = params.page || 1;
//                 console.log('data: ', data);
//                 return {
//                   results: data.results
//                 };
//             }
//
//         }
//     })
//}

