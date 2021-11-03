
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    subjectModal();
    getSubjects();
    saveSubject();
    editSubject();
    deleteSubject();
    //searchSubject();
    searchDepartment();
    departmentChange();
    //classChange();
    //deleteSubject();
})
function subjectModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#subjectModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
      $('#department-frm').empty();
      $('#department-code').val('');
      $('#subject-form')[0].reset();
      $('#subjectCode').val('');
}
function deleteSubject() {
    $('#subjectTable').on('click','.btn-deleteSubject',function (s) {
        var data = $(this).closest('tr').find('#delete-subject').val();
        bootbox.confirm("Are you sure want to delete this Subject?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteSubject/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getSubjects()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getSubjects() {
     $.ajax({
        type: 'GET',
        url: 'getSubjects',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#subjectTable').DataTable().destroy();
       $("#subjectTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#subjectTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.subjectShtCode + "</td>"
                    + "<td>" + item.subjectName + "</td>"
                    + "<td>" + item.subjectDepartment + "</td>"
                    + "<td>" + item.subjectOrder + "</td>"
                    + "<td>" + item.subjectMultiplyBy + "</td>"
                    + "<td>" + item.subjectIncludeForPos + "</td>"
                    + "<td>" + '<form id="editSubject" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-subject" name="id" value=' + item.subjectCode + '></form><button class="btn btn-outline-primary btn-sm btn-editSubject" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteSubject" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-subject" name="id" value=' + item.subjectCode + '></form><button class="btn btn-outline-danger btn-sm btn-deleteSubject" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#subjectTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveSubject(){
    $('#saveSubject').click(function () {
        var data=$('#subject-form').serialize();
        var url = '';
        if($('#subjectCode').val()===''){
          url = 'createSubject'
        }else{
            url = 'updateSubject/'+$('#subjectCode').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getSubjects()
            clearData()
            $('#subjectModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editSubject(){
    $('#subjectTable').on('click','.btn-editSubject',function (s) {
        var data=$(this).closest('tr').find('#edit-subject').val();
        $.ajax({
            type: 'GET',
            url: 'editSubject/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#subjectCode').val(s.subjectCode);
            $('#subjectShtCode').val(s.subjectShtCode);
            $('#subjectName').val(s.subjectName);
            $('#subjectOrder').val(s.subjectOrder);
            $('#subjectMultiplyBy').val(s.subjectMultiplyBy);
            //alert(s.subjectIncludeForPos);
            if (s.subjectIncludeForPos === true) {
                $('#subjectIncludeForPos').prop('checked', true);
            }
            else {
                $('#subjectIncludeForPos').prop('checked', false);

            }


            if (s.subjectDepartmentCode) {
                $('#department-code').val(s.subjectDepartmentCode)

                var $newOption = $("<option selected='selected' value='" + s.subjectDepartmentCode + "'>'+s.subjectDepartmentName+'</option>").val(s.subjectDepartmentCode.toString()).text(s.subjectDepartmentName)

                $('#department-frm').append($newOption).trigger('change');
            } else {
                $('#department-code').val('')

                $('#department-frm').empty();

            }

        $('#subjectModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
function searchDepartment() {
     $('#department-frm').select2({
           placeholder: 'Departments',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchDepartment',
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
//function searchClasses() {
//     $('#class-frm').select2({
//           placeholder: 'Classes',
//           allowClear: true,
//           width: '100%' ,
//           ajax: {
//             delay: 250,
//             url: 'searchclasses',
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
function departmentChange(){
    $('#department-frm').on('select2:select', function (e) {
    var data = e.params.data;
    $('#department-code').val(data.id)
    $('#department-name').val(data.text)

});
    $("#department-frm").on("select2:unselecting", function(e) {
    $('#department-code').val('')
    $('#department-name').val('')
 });
}
//function classChange(){
//    $('#class-frm').on('select2:select', function (e) {
//    var data = e.params.data;
//    $('#next-id').val(data.id)
//    $('#next-name').val(data.text)
//
//});
//    $("#class-frm").on("select2:unselecting", function(e) {
//    $('#next-id').val('')
//    $('#next-name').val('')
// });
//}
